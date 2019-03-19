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
    start_urls = get_start_url()[2:3]
    n = 1

    def parse(self, response):
        origin_url = response.url  # 来源url
        name = response.xpath('//p[@class="s_name"]/text()').extract()[0]  # 学校名称
        """分校信息"""
        branch_schools = response.xpath('//body/script[@type="text/javascript"]/text()').extract()[0]
        branch_schools = branch_schools.replace('var agencyTeach = ', '').replace(';', '').replace(' ', '')
        branch_schools = json.loads(branch_schools)
        branch_schools = branch_schools['teachList']
        """学校照片list"""
        img_urls = response.xpath('//div[@class="sdml_imglist"]/a/img/@src').extract()  # 学校照片(list)
        img_urls = list(map(lambda url: 'https:'+url, img_urls))
        """学校logo"""
        logo_urls = response.xpath('////div[@class="cd_info_sign"]/img/@src').extract()
        logo_urls = list(map(lambda url: 'https:'+url, logo_urls))
        school_area_type = 0  # 校区类型 0:主校区 1:分校区'
        origin_level = response.xpath('//p[@class="s_lv"]/label/text()').extract()[0]  # 来源级别

        item = GoodSchoolHomePageItem()
        item['origin_url'] = origin_url
        item['name'] = name
        item['branch_schools'] = branch_schools
        item['school_area_type'] = school_area_type
        item['origin_level'] = origin_level
        yield item

        logo_item = GoodSchoolImgItem()
        if logo_urls:
            logo_item['img_urls'] = logo_urls
            yield logo_item

        img_item = GoodSchoolImgItem()
        if img_urls:
            img_item['img_urls'] = img_urls
            yield img_item
