# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParttimejobdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    home_Img = scrapy.Field()
    home_title = scrapy.Field()
    home_href = scrapy.Field()
    home_peopleNum = scrapy.Field()
    home_perice = scrapy.Field()
    home_Address = scrapy.Field()
    home_WorkTime = scrapy.Field()
    home_Join = scrapy.Field()
    home_activityStatus = scrapy.Field()
    home_moreLink = scrapy.Field()

    Work_One = scrapy.Field()
    Work_Two = scrapy.Field()
    Work_Three = scrapy.Field()
    Work_Four = scrapy.Field()
    Work_Five = scrapy.Field()
    Work_Six = scrapy.Field()
    Work_Seven = scrapy.Field()
    Work_eight = scrapy.Field()
    Work_nine = scrapy.Field()




