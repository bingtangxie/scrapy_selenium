# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesPipeline(object):
    def process_item(self, item, spider):
        # return item
        print(item)
        # print(spider.settings['BOT_NAME'])
        # print(spider.chrome)
        # pass