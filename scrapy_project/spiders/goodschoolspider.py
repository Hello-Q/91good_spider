import scrapy
import json
import re
from ..items import *


def get_start_url():
    with open('/home/zhangyanqing/python/work/scrapy_project/file/shcool.txt') as f:
        start_url = f.read().split(', ')
        return start_url


class GoodSchoolSpider(scrapy.Spider):
    name = '91good_school'
    # start_urls = get_start_url()[5:8]
    start_urls = ['https://www.91goodschool.com/school/3698.html']
    n = 1

    def parse(self, response):
        """基础信息"""
        origin_url = response.url  # 来源url
        name = response.xpath('//p[@class="s_name"]/text()').extract()[0]  # 学校名称
        school_area_type = 0  # 校区类型 0:主校区 1:分校区'
        origin_level = response.xpath('//p[@class="s_lv"]/label/text()').extract()[0]  # 来源级别

        item = GoodSchoolHomePageItem()
        item['origin_url'] = origin_url
        item['name'] = name
        item['school_area_type'] = school_area_type
        item['origin_level'] = origin_level
        item['description'] = ''
        item['img_url'] = ''
        yield item
        """分校信息"""
        branch_schools = response.xpath('//body/script[@type="text/javascript"]/text()').extract()[0]
        branch_schools = branch_schools.replace('var agencyTeach = ', '').replace(';', '').replace(' ', '')
        branch_schools = json.loads(branch_schools)
        branch_schools = branch_schools['teachList']

        item = BranchSchoolsItem()
        item['origin_url'] = origin_url
        item['branch_school_info'] = branch_schools
        yield item

        """学校logo"""
        logo_urls = response.xpath('////div[@class="cd_info_sign"]/img/@src').extract()
        logo_urls = list(map(lambda url: 'https:' + url, logo_urls))

        logo_item = ImgItem()
        logo_item['img_urls'] = logo_urls
        logo_item['img_type'] = 'logo'
        logo_item['origin_url'] = origin_url
        yield logo_item

        """学校照片list"""
        img_urls = response.xpath('//div[@class="sdml_imglist"]/a/img/@src').extract()  # 学校照片(list)
        img_urls = list(map(lambda url: 'https:' + url, img_urls))

        img_item = ImgItem()
        img_item['img_urls'] = img_urls
        img_item['img_type'] = 'env'
        img_item['origin_url'] = origin_url
        yield img_item

        nav_name = response.xpath('//div[@class="cd_schoolNav"]/ul/li/a/text()').extract()
        nav_url = response.xpath('//div[@class="cd_schoolNav"]/ul/li/a/@href').extract()
        nav_url = list(map(lambda url: 'https://www.91goodschool.com/' + url, nav_url))
        nav_dict = dict(zip(nav_name, nav_url))
        if '学校介绍' in nav_dict.keys():
            yield scrapy.Request(nav_dict['学校介绍'], callback=self.intro, meta={'origin_url': origin_url})
        if '课程列表' in nav_dict.keys():
            yield scrapy.Request(nav_dict['课程列表'], callback=self.lesson, meta={'origin_url': origin_url})
        if '师资力量' in nav_dict.keys():
            yield scrapy.Request(nav_dict['师资力量'], callback=self.teacher, meta={'origin_url': origin_url})

    def intro(self, response):
        """处理学校介绍"""
        description = response.xpath('//div[@class="Introduce_article"]').extract()
        item = DescriptionItem()
        item['description'] = description
        item['origin_url'] = response.meta['origin_url']
        return item

    def lesson(self, response):
        """处理课程信息"""

    def teacher(self, response):
        pass
