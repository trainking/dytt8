# -*- coding: utf-8 -*-

# author:yield

import scrapy


class Dytt8Item(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    download = scrapy.Field()
