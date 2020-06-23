import requests
import json
from lxml import etree

class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q---543C897A37771FEB5ED0E8A02B4190C4:FG=1--1-3-0--1--wapp_1591596638090_312/m?kw="+tieba_name+"&pn=0"
        self.part_url = "http://tieba.baidu.com/mo/q---543C897A37771FEB5ED0E8A02B4190C4:FG=1--1-3-0--1--wapp_1591596638090_312/"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
    def parse_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode()
    def get_content_list(self,html_str):
        html = etree.Html(html_str)
        div_list = html.xpath("//div[contains@class,'i']")
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath(".a/text()")[0] if len(div.xpath(".a/text()"))>0 else None
            item["href"] = self.part_url+div.xpath(".a/@href")[0] if len(div.xpath(".a/@href"))>0 else None

        print('div_list',item["title"],item["href"])



if __name__ == '__main__':
    TiebaSpider = TiebaSpider()
    TiebaSpider.get_content_list()