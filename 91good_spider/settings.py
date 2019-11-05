# -*- coding: utf-8 -*-

# Scrapy settings for 91good_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import datetime
import random
import os
BOT_NAME = '91good_spider'

SPIDER_MODULES = ['91good_spider.spiders']
NEWSPIDER_MODULE = '91good_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = '91good_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(0.3, 1)
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    '91good_spider.middlewares.ScrapyProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # '91good_spider.middlewares.ScrapyProjectDownloaderMiddleware': 543,
   '91good_spider.middlewares.RotateUserAgentMiddleware': 543,  # 启用代理UA
   '91good_spider.middlewares.IPPOOlS': 544,  # 启用代理IP

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # '91good_spider.pipelines.ScrapyProjectPipeline': 300,
   # '91good_spider.pipelines.DownImgPipeline': 300,  # 下载图片
   # '91good_spider.pipelines.GoodSchoolPipeline': 301,  # 入库学校学校首页信息
   # '91good_spider.pipelines.BranchSchoolsPipeline': 304,  # 入库分校信息
   # '91good_spider.pipelines.SchoolDescriptionPipeline': 305,  # 入库学校简介
   '91good_spider.pipelines.LessonInfoPipeline': 306,  # 落地课程信息
   # '91good_spider.pipelines.SaveImgPipeline': 307,  # 入库学校照片链接
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 启用log
# to_day = datetime.datetime.now()
# log_file_path = './log/scrapy {}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
# LOG_LEVEL = 'WARNING'
# LOG_FILE = log_file_path

#
#
IMAGES_URLS_FIELD = "img_urls"  # 对应item里面设定的字段，取到图片的url
IMAGES_RESULT_FIELD = "image_path"
prodir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(prodir, 'file')
