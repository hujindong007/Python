# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import json

class ParttimejobdemoPipeline:
    def __init__(self):
        self.f = open('PartTimeJob.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # print("process_item",item)

        item['Work_One'] = self.process_content(item['Work_One'])
        item['Work_Two'] = self.process_content(item['Work_Two'])
        item['Work_Three'] = self.process_content(item['Work_Three'])
        item['Work_Four'] = self.process_content(item['Work_Four'])
        item['Work_Five'] = self.process_content(item['Work_Five'])
        item['Work_Six'] = self.process_content(item['Work_Six'])
        item['Work_Seven'] = self.process_content(item['Work_Seven'])
        item['Work_eight'] = self.process_content(item['Work_eight'])
        item['Work_nine'] = self.process_content(item['Work_nine'])
        self.f.write(json.dumps(dict(item), ensure_ascii=False,indent=4) + ',\n')
        return item

    def process_content(self, content):
        # 对内容项里的\xa0 和 空白字符替换为空
        content = content.strip().replace('\n', '').replace(' ', '').replace('\r', '').replace('\t', '')
        return content

    # home_Img = scrapy.Field()
    # home_title = scrapy.Field()
    # home_href = scrapy.Field()
    # home_peopleNum = scrapy.Field()
    # home_perice = scrapy.Field()
    # home_Address = scrapy.Field()
    # home_WorkTime = scrapy.Field()
    # home_Join = scrapy.Field()
    # home_activityStatus = scrapy.Field()
    # home_moreLink = scrapy.Field()
    #
    # Work_One = scrapy.Field()
    # Work_Two = scrapy.Field()
    # Work_Three = scrapy.Field()
    # Work_Four = scrapy.Field()
    # Work_Five = scrapy.Field()
    # Work_Six = scrapy.Field()
    # Work_Seven = scrapy.Field()
    # Work_eight = scrapy.Field()
    # Work_nine = scrapy.Field()
