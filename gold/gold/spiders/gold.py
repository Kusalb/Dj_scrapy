# -*- coding: utf-8 -*-
import scrapy
from ..items import GoldItem


class GoldSpider(scrapy.Spider):
    name = 'gold'
    start_urls = ['http://www.fenegosida.org/']

    def parse(self, response):
        item = GoldItem()
        price = response.css('b').css('::text').extract()
        info = response.css('#header-rate p').css('::text').extract()
        date = response.css('.rate-date div').css('::text').extract()
        count = 0
        product = []
        weight = []
        currency = []
        price =[]
        datee = []

        for i in info:
            if (count%6 ==0):
                product.append(i)
            count += 1

        for i in info:
            if (count % 6 == 1):
                weight.append(i)
            count += 1

        for i in info:
            if (count % 6 == 4):
                price.append(i)
            count += 1

        datee = date[1] + ' '+ date[0] +', ' +date[2]

        print(datee)
        item['product'] = product
        item['weight'] = weight
        # items['currency'] = currency
        item['price'] = price
        item['datee'] = datee
        yield item

