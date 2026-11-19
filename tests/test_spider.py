"""Offline parser regression tests; no real web scraping occurs."""
import importlib.util
from pathlib import Path
import unittest

from scrapy.http import HtmlResponse, Request

MODULE_PATH = Path(__file__).resolve().parents[1] / "StackExchangeAnalysis" / "StackExPoliticsSpider.py"
spec = importlib.util.spec_from_file_location("stack_ex_politics", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Spider = module.StackExPoliticsSpider


def html_response(url, html):
    return HtmlResponse(
        url=url,
        body=html.encode("utf-8"),
        encoding="utf-8",
        request=Request(url),
    )


class StackExchangeScraperTests(unittest.TestCase):
    def test_start_url_is_required_and_validated(self):
        with self.assertRaises(ValueError):
            Spider()
        with self.assertRaises(ValueError):
            Spider(start_url="javascript:bad")
        spider = Spider(start_url="http://127.0.0.1:8080/questions")
        self.assertEqual(spider.allowed_domains, ["127.0.0.1"])

    def test_number_parser(self):
        self.assertEqual(module.number_from_text("1,234 votes"), 1234)
        self.assertEqual(module.number_from_text("2.5k"), 2500)
        self.assertIsNone(module.number_from_text("no votes"))

    def test_listing_and_detail(self):
        spider = Spider(start_url="https://example.com/questions")
        listing = html_response(
            "https://example.com/questions",
            """<div class="question-summary">
                 <h3><a class="question-hyperlink" href="/q/1">First question</a></h3>
                 <div class="excerpt">Example <b>excerpt</b></div>
                 <a class="post-tag">economics</a>
                 <div class="vote-count-post"><strong>15</strong></div>
                 <div class="status"><strong>2</strong></div>
               </div>
               <a rel="next" href="/questions?page=2">Next</a>""",
        )
        requests = list(spider.parse(listing))
        self.assertEqual(len(requests), 2)
        detail_request = requests[0]
        self.assertEqual(detail_request.url, "https://example.com/q/1")
        self.assertEqual(requests[1].url, "https://example.com/questions?page=2")
        item = detail_request.cb_kwargs["summary"]
        self.assertEqual(item["title"], "First question")
        self.assertEqual(item["votes"], 15)
        self.assertEqual(item["answers_count"], 2)
        self.assertEqual(item["tags"], ["economics"])
        detail = html_response(
            detail_request.url,
            """<time datetime="2023-10-31T12:00:00Z"></time>
               <div class="user-details"><a href="/users/1">Example user</a></div>
               <div class="reputation-score">1,530</div>
               <ul><li class="comment js-comment">One</li><li class="comment">Two</li></ul>""",
        )
        parsed = list(spider.parse_question(detail, item))
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["comments_count"], 2)
        self.assertEqual(parsed[0]["user_reputation"], 1530)
        self.assertEqual(parsed[0]["user_profile_link"], "https://example.com/users/1")


if __name__ == "__main__":
    unittest.main()
