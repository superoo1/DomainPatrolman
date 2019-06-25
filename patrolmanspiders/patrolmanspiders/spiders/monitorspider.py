# -*- coding: utf-8 -*-
import scrapy

from patrolmanspiders.WebsiteEye.features_extraction import look_url
from scrapy_redis.spiders import RedisSpider

class MonitorspiderSpider(scrapy.Spider):
    name = 'monitorspider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://8153673.com/?aff=999313']

    def parse(self, response):

        pass


