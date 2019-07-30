# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    companyName = scrapy.Field()
    companySize = scrapy.Field()
    companyType = scrapy.Field()
    workingExp = scrapy.Field()
    welfare= scrapy.Field()
    city = scrapy.Field()
    time = scrapy.Field()
    idName = scrapy.Field()
    url = scrapy.Field()
    info = scrapy.Field()
    email = scrapy.Field()
    pass

class CitysItem(scrapy.Item):
    city = scrapy.Field()


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    releaseDate = scrapy.Field()
    typeId = scrapy.Field()


class sItems(scrapy.Item):
    position_category = scrapy.Field()
    positon_name = scrapy.Field()
    position_nature = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    city = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    position_advantage = scrapy.Field()
    position_address = scrapy.Field()
    position_desc = scrapy.Field()
    update_time = scrapy.Field()
    company_name = scrapy.Field()
    company_features = scrapy.Field()
    has_labels = scrapy.Field()
    industry_field = scrapy.Field()
    company_size = scrapy.Field()
    company_url = scrapy.Field()
    url = scrapy.Field()