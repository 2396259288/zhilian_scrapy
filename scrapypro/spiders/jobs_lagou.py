# -*- coding: utf-8 -*-
import scrapy,json
from scrapypro.items import JobsItem

class JobsSpider(scrapy.Spider):
    name = 'lagoujobs'
    # allowed_domains = ['m.lagou.com']
    
    offset = 1
    start_urls = ['https://m.lagou.com/listmore.json?pageNo='+str(offset)+'&pageSize=15']
    

    def parse(self, response):
        if self.offset == 100:
            return
        data = json.loads(response.text)
        results = data['content']['data']['page']['result']
        for result in results:
            item = JobsItem()
            item['name'] = result['positionName']
            item['salary'] = result['salary']
            item['companyName'] = result['companyFullName']
            item['city'] = result['city']
            item['time'] = result['createTime']
            item['idName'] = result['positionId']
            item['url'] = 'https://m.lagou.com/jobs/'+str(result['positionId'])+'.html'
            yield item   
        self.offset += 1
        yield scrapy.Request('https://m.lagou.com/listmore.json?pageNo='+str(self.offset)+'&pageSize=15', callback = self.parse)