# -*- coding: utf-8 -*-
import scrapy
import logging as log
import re
from feedreader.items import FeedreaderItem


class FeedreaderspiderSpider(scrapy.Spider):
    name = "feedreaderspider"
    allowed_domains = ["feedreader.com"]
    start_urls = ['http://feedreader.com/']

    def parse(self, response):
        news_list = response.xpath('//div[contains(@class, "news-list")]/ul/li')
        for each_news in news_list:
            item = FeedreaderItem()
            news_title = each_news.xpath('div/p/a/text()').extract()
            news_date = each_news.xpath('div/span/text()').extract()
            news_link = each_news.xpath('div/p/a/@href').extract()
            news_short_description = each_news.xpath('div/div/p/text()').extract()
            description = ''
            for desc in news_short_description:
                description += desc.strip()
            item['news_title'] = news_title[0]
            item['news_date'] = news_date[0]
            item['news_link'] = 'http:%s' % news_link[0]
            item['news_short_description'] = description
            request = scrapy.Request(url=item['news_link'], callback=self.parse_url)
            request.meta['item'] = item
            yield request

    # This method is called with news response and get the news read count
    def parse_url(self, response):
        item = response.meta['item']
        count_read_list = response.xpath('//div[contains(@class, "links")]/text()').extract()
        count = 0
        for count_read in count_read_list:
            tokens = count_read.split(' ')
            for token in tokens:
                if token.isdigit():
                    count = token
        item['news_read_count'] = count
        yield item



