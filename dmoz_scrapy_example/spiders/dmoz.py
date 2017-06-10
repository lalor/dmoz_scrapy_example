# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = ['http://dmoztools.net/']

    def parse(self, response):
        pass
