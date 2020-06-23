# -*- coding: utf-8 -*-
import scrapy


class ParttimejobSpider(scrapy.Spider):
    name = 'partTimeJob'
    allowed_domains = ['zjcampus.com']
    start_urls = ['http://zjcampus.com/']

    def parse(self, response):
        pass
