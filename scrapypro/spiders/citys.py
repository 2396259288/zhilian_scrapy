# -*- coding: utf-8 -*-
import scrapy
# from scrapypro.items import CitysItem

class CitySpider(scrapy.Spider):
    name = 'tb'
    print('-' * 20)
    start_urls = ['https://www.zhaopin.com/']
    print('+' * 20)
    def parse(self, response):
        print(response.text[:500])
        print('*' * 20)
        # city_lists = response.xpath('//*[@id="root"]/div[2]/div[3]/div/ul/li/a/text()').extract()
        # for city in city_lists:
        #     item = CitysItem()
        #     item['city'] = city.strip()
        #     yield item



