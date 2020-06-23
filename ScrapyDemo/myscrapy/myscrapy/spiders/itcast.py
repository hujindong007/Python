# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名
    allowed_domains = ['itcast.cn'] #允许爬虫范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']#最开始请求的url地址
    #parse 不能修改
    def parse(self, response):
        # item = response.xpath("//div[@class='tea_con']//h3/text()")
        # item = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(item)

        #分组
         li_list = response.xpath("//div[@class='tea_con']//li")
         for li in li_list:
             item = {}
             item["name"] = li.xpath(".//h3/text()").extract_first()
             item["Level"] = li.xpath(".//h4/text()").extract_first()
             # print(item)

             yield item #yield每次遍历逐个读取到内存中，不会导致内存飙升
