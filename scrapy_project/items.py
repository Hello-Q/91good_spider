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
    # 学校首页
    origin_url = scrapy.Field()
    name = scrapy.Field()
    branch_schools = scrapy.Field()
    school_area_type = scrapy.Field()
    origin_level = scrapy.Field()
    img_url = scrapy.Field()
    description = scrapy.Field()


class ImgItem(scrapy.Item):
    # 图片处理(下载独立图片如logo,环境img_list)
    img_urls = scrapy.Field()
    image_paths = scrapy.Field()
    img_type = scrapy.Field()
    origin_url = scrapy.Field()


class BranchSchoolsItem(scrapy.Item):
    # 分校信息
    branch_school_info = scrapy.Field()
    origin_url = scrapy.Field()


class DescriptionItem(scrapy.Item):
    # 学校介绍
    description = scrapy.Field()
    img_urls = scrapy.Field()
    # image_paths = scrapy.Field()
    # img_type = scrapy.Field()
    origin_url = scrapy.Field()


class LessonInfoItem(scrapy.Item):
    """课程信息"""
    name = scrapy.Field()
    price = scrapy.Field()
    tag = scrapy.Field()
    description = scrapy.Field()
    img_urls = scrapy.Field()
    image_paths = scrapy.Field()
    img_type = scrapy.Field()
    origin_url = scrapy.Field()
