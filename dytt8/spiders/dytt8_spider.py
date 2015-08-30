# -*- coding: utf-8 -*-

# author:yield

import scrapy

from dytt8.items import Dytt8Item
from dytt8.db import sqliteDB


class Dytt8Spider(scrapy.Spider):
    name = "dytt8"
    allowed_domains = ['dytt8.com']
    start_urls = [
        "http://www.dytt8.net/html/gndy/dyzz/20150824/48848.html"
    ]

    def parse(self, response):
        dytt8 = Dytt8Item()
        dytt8['url'] = response.url
        dytt8['name'] = response.xpath("//title/text()").extract()[0]
        dytt8['download'] = response.xpath("//td[@bgcolor='#fdfddf']/a/text()").extract()[0]
        sqliteDB.add(dytt8)
        return dytt8