# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GoodSchoolHomePageItem(scrapy.Item):
    origin_url = scrapy.Field()
    name = scrapy.Field()
    branch_schools = scrapy.Field()
    school_area_type = scrapy.Field()
    origin_level = scrapy.Field()


class GoodSchoolImgItem(scrapy.Item):
    img_urls = scrapy.Field()
    image_paths = scrapy.Field()

