# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class ItcastspiderPipeline:

    def __init__(self):
        self.file = open("tearch2.json",'w',encoding='utf-8')
    def process_item(self, item, spider):
        content =json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(content)

        return item
    def close_spider(self,spider):
        self.file.close()