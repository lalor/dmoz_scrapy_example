# -*- coding: utf-8 -*-
from __future__ import print_function
import scrapy

from dmoz_scrapy_example.items import DmozScrapyExampleItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Resources/',
                    'http://dmoztools.net/Computers/Programming/Languages/Python/Books/']

    def parse(self, response):

        item = DmozScrapyExampleItem()
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item['title'] = sel.xpath('./a/div/text()').extract()[0] # 标题
            item['link'] = sel.xpath('./a/@href').extract()[0] # 链接
            item['desc'] = sel.xpath('./div/text()').extract()[0].strip() # 详细描述
            yield item
