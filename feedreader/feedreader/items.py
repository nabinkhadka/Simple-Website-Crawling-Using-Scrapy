# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeedreaderItem(scrapy.Item):
    # define the fields for your item here like:
    news_title = scrapy.Field()
    news_date = scrapy.Field()
    news_link = scrapy.Field()
    news_short_description = scrapy.Field()
    news_read_count = scrapy.Field()
    pass
