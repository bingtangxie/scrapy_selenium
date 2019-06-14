# -*- coding: utf-8 -*-
import scrapy
from quotes.items import QuotesItem
from scrapy import signals
from selenium import webdriver


class Demo01Spider(scrapy.Spider):
    name = 'demo01'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # spider = super(Demo01Spider, cls).from_crawler(crawler, *args, **kwargs)
        # crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        spider = cls(*args, **kwargs)
        spider.set_crawler(crawler)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        spider.chrome = webdriver.Chrome()
        return spider

    def parse(self, response):
        items = QuotesItem()
        quotes = response.xpath("//div[@class='quote']")
        for item in quotes:
            quote = item.xpath("./span[@class='text']/text()").extract()[0]
            author = item.xpath("./span")[1].xpath("./small[@class='author']/text()").extract()[0]
            items["quote"] = quote
            items["author"] = author
            yield items

    @classmethod
    def spider_closed(cls, spider):
        print("closed !!!")
        spider.chrome.close()
