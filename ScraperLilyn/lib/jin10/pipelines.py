# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# 存放数据的列表
data_list = []
class HaiwaiPipeline:
    def open_spider(self, spider):
        if spider.name == "gu":
            print("爬虫开始")
    def process_item(self, item, spider):
        if spider.name == "gu":
            data_list.append(item)
    def close_spider(self, spider):
        with open('jin10chinese.json', 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)







