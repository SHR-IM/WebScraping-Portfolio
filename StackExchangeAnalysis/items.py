# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StackExPoliticsItem(scrapy.Item):
    title = scrapy.Field()
    question_link = scrapy.Field()
    tags = scrapy.Field()
    votes = scrapy.Field()
    answers_count = scrapy.Field()
    comments_count = scrapy.Field()     
    excerpt = scrapy.Field()
    asked_time = scrapy.Field()
    user_name = scrapy.Field()
    user_profile_link = scrapy.Field()
    user_reputation = scrapy.Field()
    user_gold_badges = scrapy.Field()
    user_silver_badges = scrapy.Field()
    user_bronze_badges = scrapy.Field()