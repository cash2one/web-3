# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs


class DemoScrapyPipeline(object):
    """
    通过Feed exports保存信息（默认）
    scrapy crawl *** -o ***.json -t json
    -o 导出文件名
    -t 导出类型（JSON，JSON lines，CSV，XML）
    """

    def process_item(self, item, spider):
        return item


class JsonWithEncodingJobPipeline(object):
    """
    scrapy crawl ***
    """

    def __init__(self):
        self.file = codecs.open('job.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
