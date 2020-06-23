# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyscrapyPipeline:
    # process_item 不能修改 一定要有
    def process_item(self, item, spider):
        item["hello"] = "word"
        # print(item)
        return item #先走的必须return 不然后输出为none
#会发现 先走 MyscrapyPipeline 再走MyscrapyPipeline1  要在setting中设置数值
class MyscrapyPipeline1:
    def process_item(self, item, spider):
        print(item)
        return item