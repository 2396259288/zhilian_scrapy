# -*- coding: utf-8 -*-
import scrapy,json
from scrapypro.items import JobsItem

class JobsSpider(scrapy.Spider):
    name = 'zljobs'
    # allowed_domains = ['m.lagou.com']
    
    offset = 0
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start='+str(offset)+'&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&_v=0.30038094&x-zp-page-request-id=6278ef5e9bdd474bbdbdab558aec6f16-1556775610651-998866']
    

    def parse(self, response):
        if self.offset == 1080:
            return 
        data = json.loads(response.text)
        results = data['data']['results']
        for result in results:
            item = JobsItem()
            item['name'] = result['jobName']
            item['salary'] = result['salary']
            item['companyName'] = result['company']['name']
            item['companySize'] = result['company']['size']['name']
            item['companyType'] = result['company']['type']['name']
            city = result['city']['display']
            if len(city) > 4:
                item['city'] = city.split('-')[0]
            else:
                item['city'] = city
            item['time'] = result['updateDate']
            item['idName'] = result['number']
            item['workingExp'] = result['workingExp']['name']
            item['welfare'] = result['welfare']
            item['url'] = result['positionURL']
            item['email'] = '994071021@qq.com'
            # yield item
            yield scrapy.Request(item['url'], meta = {'item':item}, callback = self.parse1)   
        self.offset += 90
        yield scrapy.Request('https://fe-api.zhaopin.com/c/i/sou?start='+str(self.offset)+'&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&_v=0.30038094&x-zp-page-request-id=6278ef5e9bdd474bbdbdab558aec6f16-1556775610651-998866', callback = self.parse)



    def parse1(self, response):
        item = response.meta['item']
        item['info'] = response.xpath('//*[@id="root"]/div[4]/div[1]/div[1]/div[2]/div').extract()[0]
        yield item