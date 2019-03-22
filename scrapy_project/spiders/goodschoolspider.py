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
    start_urls = get_start_url()
    # start_urls = ['https://www.91goodschool.com/school/3310.html']
    n = 1

    def parse(self, response):
        """基础信息"""
        print('开始处理第', self.n, '条信息, 共',len(self.start_urls), '条信息')
        self.n += 1
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
            yield scrapy.Request(nav_dict['课程列表'], callback=self.lesson_url, meta={'origin_url': origin_url})
        # if '师资力量' in nav_dict.keys():
        #     yield scrapy.Request(nav_dict['师资力量'], callback=self.teacher_url, meta={'origin_url': origin_url})

    def intro(self, response):
        """处理学校介绍"""
        print('处理学校介绍')
        description = response.xpath('//div[@class="Introduce_article"]').extract()[0]
        img_urls = response.xpath('//div[@class="Introduce_article"]//img').extract()
        item = DescriptionItem()
        item['img_urls'] = img_urls
        item['description'] = description
        item['origin_url'] = response.meta['origin_url']
        return item

    def lesson_url(self, response):
        """返回课程url"""
        # 课程list
        course_urls = response.xpath('//ul[@class="JG-list"]/li/div/div[@class="imgdiv"]/a/@href').extract()
        course_urls = list(map(lambda url: 'https://www.91goodschool.com' + url, course_urls))
        # 发送课程详情url
        for course_url in course_urls:
            yield scrapy.Request(course_url, callback=self.lesson, meta={'origin_url': response.meta['origin_url']})

    def lesson(self, response):
        print('开始处理课程信息')
        name = response.xpath('//div[@class="info_couName"]/h1/text()').extract()[0]
        price = response.xpath('//label[@class="coursePrice"]/text()').extract()[0]
        tag = response.xpath('//div[@class="info_studType"]/label/text()').extract()
        description = response.xpath('//div[@class="cdml_coursedetail"]').extract()[0]
        img_urls = response.xpath('//div[@class="cdml_coursedetail"]//img').extract()

        item = LessonInfoItem()
        item['name'] = name
        item['price'] = price
        item['tag'] = tag
        item['description'] = description
        item['img_urls'] = img_urls
        item['origin_url'] = response.meta['origin_url']
        yield item

    # def teacher_url(self, response):
    #     # 教师url list
    #     teacher_urls = response.xpath('//ul[@class="info-list"]/li/a/@href').extract()
    #     if teacher_urls:
    #         for teacher_url in teacher_urls:
    #             yield scrapy.Request(teacher_url, self.teacher, meta={'origin_url': response.meta['origin_url']})
    #
