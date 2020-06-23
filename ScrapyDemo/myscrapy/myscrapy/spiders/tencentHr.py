# -*- coding: utf-8 -*-
import scrapy


class TencenthrSpider(scrapy.Spider):
    name = 'tencentHr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        div_list = response.xpath("//div[@class='recruit-list']")
        print("div_list",div_list)
        # for div in div_list:
        #     item = {}
        #     item["title"] = div.xpath(".//h4/text()").extract_first()
        #     print(item)


# 在终端运行 输入scrapy crawl tencentHr

