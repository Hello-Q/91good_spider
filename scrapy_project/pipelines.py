# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
# 导入这个包为了移动文件
import shutil
import json


class ScrapyProjectPipeline(object):

    def process_item(self, item, spider):
        return item


class GoodSchoolPipeline(object):

    def process_item(self, item, spider):
        print(item, type(item))
        item = dict(item)
        print(item, type(item))
        return item



class GoodSchoolImgPipeline(ImagesPipeline):
    """图片下载,列表传url"""
    def get_media_requests(self, item, info):
        if 'img_urls' in [i for i in item.keys()]:
            for image_url in item['img_urls']:
                yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        if 'img_urls' in [i for i in item.keys()]:
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            item['image_paths'] = image_paths



