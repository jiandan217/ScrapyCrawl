# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #价格
    price = scrapy.Field()
    #颜色
    color = scrapy.Field()
    #尺码
    size = scrapy.Field()
    #网站货号
    sku = scrapy.Field()
    #详情
    details =scrapy.Field()
    #大图url
    img_urls =scrapy.Field()
