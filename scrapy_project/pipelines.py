# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
import pymysql
from scrapy.utils.project import get_project_settings
# 导入这个包为了移动文件
import shutil
import json
from .items import *


class Mysql:
    db = None

    def __init__(self):
        # self.db = pymysql.connect('localhost', 'root', 'ZYQ1994zyq', 'pt')
        self.db = pymysql.connect('47.110.148.144', 'root', 'rootMysqlzhengren79', 'test')

    def write_dict_data(self, data, sql):
        """
        向数据库插入字典数据
        :param data: 插入的数据
        :param sql: 执行的语句
        :return:
        """
        # 获取游标
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        # 数据列名
        cols = ', '.join('`{}`'.format(k) for k in data.keys())
        # 数据值
        val_cols = ', '.join('%({})s'.format(k) for k in data.keys())
        # sql语句
        res_sql = sql % (cols, val_cols)
        print(res_sql)
        cursor.execute(res_sql, data)
        self.db.commit()
        self.db.close()

    def write_data(self, sql):
        # 常规插入数据
        print(sql)
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        self.db.commit()
        self.db.close()
        self.db.close()

    def select_data(self, sql):
        """查询数据库数据"""
        print(sql)
        # 获取游标
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        self.db.close()
        return data


class GoodSchoolPipeline(object):
    """入库基础数据"""
    def process_item(self, item, spider):
        if isinstance(item, GoodSchoolHomePageItem):
            school_date = dict(item)
            write_data = Mysql()
            sql = "insert into school(%s) values(%s)"
            write_data.write_dict_data(school_date, sql)
        return item


class ImgPipeline(ImagesPipeline):
    """图片下载,列表传url"""
    def get_media_requests(self, item, info):
        if isinstance(item, ImgItem):
            for image_url in item['img_urls']:
                yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        if isinstance(item, ImgItem):
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            item['image_paths'] = image_paths
        return item


class SchoolImgPipeline(object):
    """保存logo以及环境图片url到数据库"""
    def process_item(self, item, spider):
        if isinstance(item, ImgItem):
            if item['img_type'] == 'logo':
                origin_url = item['origin_url']
                logo_path = dict(item)['image_paths']
                logo_name = list(map(lambda path: path.replace('full/', ''), logo_path))
                logo_url = list(map(lambda new_path: 'http://pt.njzredu.com/upload/20190320/' + new_path, logo_name))
                logo_url = dict(zip(['logo_url'], logo_url))
                write_data = Mysql()
                sql = "update school set %s=%s where origin_url='{0}'".format(origin_url)
                write_data.write_dict_data(logo_url, sql)
            if item['img_type'] == 'env':  # 环境
                origin_url = item['origin_url']
                env_paths = dict(item)['image_paths']
                env_names = list(map(lambda path: path.replace('full/', ''), env_paths))
                env_urls = list(map(lambda new_path: 'http://pt.njzredu.com/upload/20190320/' + new_path, env_names))
                env_url_list = []
                for env_url in env_urls:
                    env_url_list.append(dict(zip(['img'], [env_url])))
                img_url = dict(zip(['img_url'], [str(env_url_list)]))
                write_data = Mysql()
                sql = "update school set %s=%s where origin_url='{0}'".format(origin_url)
                write_data.write_dict_data(img_url, sql)
        return item


class BranchSchoolsPipeline(object):
    """处理分校信息入库"""
    def process_item(self, item, spider):
        if isinstance(item, BranchSchoolsItem):
            item = dict(item)
            origin_url = item['origin_url']
            select_data = Mysql()
            sql = "select id from school where origin_url='{0}'".format(origin_url)
            parent_school_id = select_data.select_data(sql)[0]['id']
            print(parent_school_id)
            data = {}
            for school_info in item['branch_school_info']:
                name = school_info['name']
                lon = school_info['lng']
                lat = school_info['lat']
                data['name'] = name
                data['lon'] = lon
                data['lat'] = lat
                data['school_area_type'] = 1
                data['parent_school_id'] = parent_school_id
                data['img_url'] = ''
                data['description'] = ''
                write_data = Mysql()
                sql = "insert into school(%s) values(%s)"
                write_data.write_dict_data(data, sql)
        return item


class SchoolDescription(object):
    def process_item(self, item, spider):
        if isinstance(item, DescriptionItem):
            item = dict(item)
            origin_url = item['origin_url']
            data = dict(zip(['description'], [item['description']]))
            print(data)
            write_data = Mysql()
            mysql = "update school set %s=%s where origin_url='{0}'".format(origin_url)
            write_data.write_dict_data(data, mysql)
            print('分校信息')
        return item

