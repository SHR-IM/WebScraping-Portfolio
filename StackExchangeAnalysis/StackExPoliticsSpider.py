import scrapy
from scrapy.loader import ItemLoader
from StackExPolitics.items import StackExPoliticsItem

class StackExPoliticsSpider(scrapy.Spider):
    name = "StackExPoliticsSpider"
    allowed_domains = ["127.0.0.1"]
    start_urls = ["http://127.0.0.1:8080/politics.stackexchange.com_en_all_2023-11/questions"]

    def parse(self, response):
        #Scraping the list of questions on the page
        questions = response.css("div.question-summary")
        for question in questions:
            question_link = question.css('h3 a.question-hyperlink::attr(href)').get()
            if question_link:
                yield response.follow(question_link,self.parse_question,meta={'question': question})

        #Scraping all pages
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page,self.parse)

    def parse_question(self, response):
        question = response.meta['question']
        loader = ItemLoader(item=StackExPoliticsItem(),selector=question)

        #Scraping fields from the question
        loader.add_css('title','h3 a.question-hyperlink::text')
        loader.add_css('question_link','h3 a.question-hyperlink::attr(href)')
        loader.add_css('excerpt','.excerpt::text')
        loader.add_css('tags','div.tags a.post-tag::text')
        loader.add_css('asked_time','.s-user-card--time::attr(datetime)')
        loader.add_css('user_name','.s-user-card--link::text')
        loader.add_css('user_profile_link','.s-user-card--avatar::attr(href)')
        loader.add_css('user_reputation','.s-user-card--rep::text')
        loader.add_css('user_gold_badges','.s-award-bling__gold::text')
        loader.add_css('user_silver_badges','.s-award-bling__silver::text')
        loader.add_css('user_bronze_badges','.s-award-bling__bronze::text')
        loader.add_css('votes','.vote-count-post strong::text')
        loader.add_css('answers_count','.status strong::text')

        #Counting comments
        comments = response.css('.comment.js-comment').getall()
        loader.add_value('comments_count',len(comments))

        yield loader.load_item()
