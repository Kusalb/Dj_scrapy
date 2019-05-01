# -*- coding: utf-8 -*-
import scrapy
from ..items import TarkariItem

class TarkariSpider(scrapy.Spider):
    name = 'tarkari'
    start_urls = [
        'http://kalimatimarket.gov.np/home/wpricelist?fbclid=IwAR3xnZcl3UR5JAoUev-no6ElvTQmJIfyOeCa90EhgaXTgH0TQzUVexWT0SY']

    def parse(self, response):
        item = TarkariItem()
        name = response.css('td:nth-child(1)').css('::text').extract()
        unit = response.css('td:nth-child(2)').css('::text').extract()
        minimum = response.css('td:nth-child(3)').css('::text').extract()
        maximum = response.css('td:nth-child(4)').css('::text').extract()
        average = response.css('td:nth-child(5)').css('::text').extract()

        item['name'] = name
        item['unit'] = unit
        item['minimum'] = minimum
        item['maximum'] = maximum
        item['average'] = average
        yield item
