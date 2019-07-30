# -*- coding: utf-8 -*-
import time
import scrapy,json
from scrapypro.items import NewsItem

class newsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['m.lagou.com']
    
    offset = 1
    start_urls = ['https://www.huodongjia.com/it/page-'+ str(offset) +'/']
    

    def parse(self, response):
        if self.offset == 10:
            return
        urls = response.xpath("/html/body/div[3]/div/div[2]/div[1]/div/div/a/@href").extract()
        for url in urls:
            yield scrapy.Request('https://www.huodongjia.com' + url, callback = self.parse1)
        self.offset += 1
        yield scrapy.Request('https://www.huodongjia.com/it/page-'+ str(self.offset) +'/', callback = self.parse)

    def parse1(self, response):
        item = NewsItem()
        title_gg = response.xpath("/html/body/div[3]/div[4]/div/div[1]/table/tr/td[2]/h1/a//text()").extract()
        title_gg.append(' ')
        title = title_gg[0].strip()    

        content_gg = response.xpath("//*[@id='meeting_1']/div/div[1]/div/div/p/text()").extract()
        content_gg.append(' ')
        content = content_gg[0].strip()
        
        author_gg = response.xpath("/html/body/div[3]/div[4]/div/div[1]/table/tr/td[2]/p[4]/span/a/text()").extract()
        author_gg.append(' ')
        author = author_gg[0].strip()
        
        releaseDate = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
        typeId = "IT互联网"
        item['title'] = title
        item['content'] = content
        item['author'] = author
        item['releaseDate'] = releaseDate
        yield item

            






            

            

