# -*- coding: utf-8 -*-
from __future__ import print_function
import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Resources/',
                    'http://dmoztools.net/Computers/Programming/Languages/Python/Books/']

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            for index, item in enumerate(response.xpath('//div[@class="title-and-desc"]'), 1):
                title = item.xpath('./a/div/text()').extract()[0] # 标题
                link = item.xpath('./a/@href').extract()[0] # 链接
                desc = item.xpath('./div/text()').extract()[0].strip() # 详细描述
                print(index, title, link, desc, sep=',', file=f)
