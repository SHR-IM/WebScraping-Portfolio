"""Scrapy spider for Stack Exchange Politics question-list snapshots.

This spider can run against an explicitly supplied URL, including a locally
served historical archive. It does not assume the local archive is available.
Scraping a live website requires respecting its robots.txt and terms.
"""
import re
from urllib.parse import urlparse

import scrapy


def number_from_text(value):
    """Parse display counts such as '1,240 votes', '2k', or '3 answers'."""
    if value is None:
        return None
    match = re.search(r"(-?\d[\d,]*(?:\.\d+)?)\s*([kKmM]?)", str(value))
    if not match:
        return None
    amount = float(match.group(1).replace(",", ""))
    factor = {"": 1, "k": 1_000, "m": 1_000_000}[match.group(2).lower()]
    return int(amount * factor)


def normalize_text(parts):
    return " ".join(" ".join(parts).split())


class StackExPoliticsSpider(scrapy.Spider):
    name = "stack_exchange_politics"

    custom_settings = {
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "DOWNLOAD_DELAY": 1.0,
        "AUTOTHROTTLE_ENABLED": True,
        "FEED_EXPORT_ENCODING": "utf-8",
    }

    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not start_url:
            raise ValueError(
                "Supply a question listing URL: -a start_url=https://.../questions"
            )
        parsed = urlparse(start_url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("start_url must be a full HTTP(S) URL")
        self.start_urls = [start_url]
        self.allowed_domains = [parsed.hostname]

    def parse(self, response):
        """Parse modern and legacy question listing markup."""
        cards = response.css("div.question-summary, div.s-post-summary")
        for card in cards:
            link = card.css(
                "h3 a.question-hyperlink::attr(href), "
                "h3 a.s-link::attr(href), "
                "a.s-post-summary--content-title::attr(href)"
            ).get()
            if not link:
                continue

            title = normalize_text(
                card.css(
                    "h3 a.question-hyperlink::text, "
                    "h3 a.s-link::text, "
                    "a.s-post-summary--content-title::text"
                ).getall()
            )
            votes = normalize_text(
                card.css(".vote-count-post ::text, .s-post-summary--stats-item-number::text").getall()
            )
            answers = normalize_text(
                card.css(".status strong::text, .s-post-summary--stats-item:has(.s-post-summary--stats-item-number) ::text").getall()
            )
            summary = {
                "title": title,
                "question_link": response.urljoin(link),
                "excerpt": normalize_text(
                    card.css(
                        ".excerpt ::text, .s-post-summary--content-excerpt ::text"
                    ).getall()
                ),
                "tags": card.css(".post-tag::text").getall(),
                "votes": number_from_text(votes),
                "answers_count": number_from_text(answers),
            }
            yield response.follow(
                link, callback=self.parse_question, cb_kwargs={"summary": summary}
            )

        next_page = response.css(
            'a[rel="next"]::attr(href), a.s-pagination--item[rel="next"]::attr(href)'
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_question(self, response, summary):
        """Enrich listing data using the linked question detail page."""
        result = dict(summary)
        result["comments_count"] = len(
            response.css(".comment.js-comment, li.comment")
        )
        result["asked_time"] = response.css(
            ".s-user-card--time::attr(datetime), time::attr(datetime)"
        ).get()
        result["user_name"] = normalize_text(
            response.css(
                ".s-user-card--link::text, .user-details a::text, "
                ".user-info .user-details a::text"
            ).getall()[:1]
        ) or None
        profile = response.css(
            ".s-user-card--link::attr(href), "
            ".user-details a::attr(href)"
        ).get()
        result["user_profile_link"] = (
            response.urljoin(profile) if profile else None
        )
        result["user_reputation"] = number_from_text(
            normalize_text(
                response.css(
                    ".s-user-card--rep::text, .reputation-score::text"
                ).getall()
            )
        )
        yield result
