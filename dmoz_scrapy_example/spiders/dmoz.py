# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Resources/',
                    'http://dmoztools.net/Computers/Programming/Languages/Python/Books/']

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
