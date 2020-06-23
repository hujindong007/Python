# -*- coding: utf-8 -*-
import scrapy
from PartTimeJobDemo.items import ParttimejobdemoItem


class ParttimejobSpider(scrapy.Spider):
    name = 'partTimeJob'
    allowed_domains = ['zjcampus.com']
    start_urls = ['http://www.zjcampus.com/event?page=1']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='am-avg-sm-1 am-avg-md-1 am-avg-lg-3']//li")
        for li in li_list:
            item = ParttimejobdemoItem()
            itemContent = li.xpath(".//div[@class='info am-gallery-overlay']//p")
            item["home_Img"] = li.xpath(".//div[@class='info am-gallery-overlay']//img/@src").extract_first()
            item["home_title"] = li.xpath(".//a[@class='am-gallery-item']/@title").extract_first()
            item["home_href"] = li.xpath(".//a[@class='am-gallery-item']/@href").extract_first()
            item["home_peopleNum"] = itemContent[0].xpath(".//span/text()").extract_first()
            item["home_perice"] = itemContent[0].xpath(".//span[@class='am-text-warning']/text()").extract_first()
            item["home_Address"] = itemContent[1].xpath(".//span/text()").extract_first()
            item["home_WorkTime"] = itemContent[2].xpath(".//span/text()").extract_first()
            item["home_Join"] = itemContent[3].xpath(".//strong[@class='am-text-warning']/text()").extract_first()
            item["home_activityStatus"] = li.xpath(".//div[@class='info am-gallery-overlay']//a/text()").extract()[3]
            item["home_moreLink"] = li.xpath(".//div[@class='info am-gallery-overlay']//p").extract()[3]
            # print(item)
            # if type(item["home_href"]) == str:
                #请求详情页
            # print(item["home_href"])
            yield scrapy.Request(
                    url=item["home_href"],dont_filter=True,callback=self.parse_detail,meta={'data':item},encoding='utf-8')


                # 下一页
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        print("next_url",next_url)
        if next_url is not None:
          yield scrapy.Request(next_url, callback=self.parse)



    # 需要所有 < p > 标签下的内容吗 需要这样写
    # xpath('//p/descendant::text()')

    # 只需要 < p > 或者 < strong > 下的内容 可以这样写xpath('//p/text()|//p/strong/text()')

    def parse_detail(self,response):
        item = response.meta['data']
        # item = ParttimejobdemoItem()
        itemContent = response.xpath(".//div[@class='event-detail am-margin-bottom white-box']//p/descendant::text()")
        item["Work_One"] = itemContent[0].extract()
        item["Work_Two"] = itemContent[1].extract()
        item["Work_Three"] = itemContent[2].extract()
        item["Work_Four"] = itemContent[3].extract()
        item["Work_Five"] = itemContent[4].extract()
        item["Work_Six"] = itemContent[5].extract()
        item["Work_Seven"] = itemContent[6].extract()
        item["Work_eight"] = itemContent[7].extract()
        item["Work_nine"] = itemContent[8].extract()
        print("itemDetail",item)
        yield item  # 对返回的数据进行处理


# 这个是 requests 直接请求
# import requests
# import json
# from lxml import etree
#
# class TiebaSpider:
#     def __init__(self,tieba_name):
#         self.tieba_name = tieba_name
#         self.start_url = "http://tieba.baidu.com/mo/q---543C897A37771FEB5ED0E8A02B4190C4:FG=1--1-3-0--1--wapp_1591596638090_312/m?kw="+tieba_name+"&pn=0"
#         self.part_url = "http://tieba.baidu.com/mo/q---543C897A37771FEB5ED0E8A02B4190C4:FG=1--1-3-0--1--wapp_1591596638090_312/"
#         self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
#     def parse_url(self,url):
#         response = requests.get(url,headers=self.headers)
#         return response.content.decode()
#     def get_content_list(self,html_str):
#         html = etree.Html(html_str)
#         div_list = html.xpath("//div[contains@class,'i']")
#         content_list = []
#         for div in div_list:
#             item = {}
#             item["title"] = div.xpath(".a/text()")[0] if len(div.xpath(".a/text()"))>0 else None
#             item["href"] = self.part_url+div.xpath(".a/@href")[0] if len(div.xpath(".a/@href"))>0 else None
#
#         print('div_list',item["title"],item["href"])
#
#
#
# if __name__ == '__main__':
#     TiebaSpider = TiebaSpider()
#     TiebaSpider.get_content_list()
