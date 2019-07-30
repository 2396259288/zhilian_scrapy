# -*- coding: utf-8 -*-
import scrapy,json
from scrapypro.items import JobsItem, sItems

class JobsSpider(scrapy.Spider):
    name = 'djjobs'
    # allowed_domains = ['m.lagou.com']
    
    offset = 0
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start='+str(offset)+'&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&_v=0.30038094&x-zp-page-request-id=6278ef5e9bdd474bbdbdab558aec6f16-1556775610651-998866']
    

    def parse(self, response):
        if self.offset == 180:
            return
        data = json.loads(response.text)
        results = data['data']['results']
        for result in results:
            item = sItems()
            item['position_category'] = result['jobType']['display']
            item['positon_name'] = result['jobName']
            item['position_nature'] = result['emplType']
            item['salary_min'] = result['salary'].split('-')[0]
            item['salary_max'] = result['salary'].split('-')[0]
            item['city'] = result['city']['display']
            item['experience'] = result['workingExp']['name']
            item['education'] = result['eduLevel']['name']
            item['position_advantage'] = '+'.join(result['welfare'])
            item['update_time'] = result['createDate']
            item['company_name'] = result['company']['name']
            item['company_size'] = result['company']['size']['name']
            item['industry_field'] = ','.join(result['extractNormalizedTag'])
            item['company_url'] = result['company']['url']
            item['has_labels'] = '+'.join(result['welfare'])
            item['company_features'] = result['jobTag']['searchTag']


            
            item['url'] = result['positionURL']
            # yield item
            yield scrapy.Request(item['url'], meta = {'item':item}, callback = self.parse1)   
        self.offset += 90
        yield scrapy.Request('https://fe-api.zhaopin.com/c/i/sou?start='+str(self.offset)+'&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&_v=0.30038094&x-zp-page-request-id=6278ef5e9bdd474bbdbdab558aec6f16-1556775610651-998866', callback = self.parse)



    def parse1(self, response):
        item = response.meta['item']
        item['position_address'] = response.xpath('//*[@id="root"]/div[4]/div[1]/div[1]/div[3]/div/span').extract()[0]
        item['position_desc'] = response.xpath('//*[@id="root"]/div[4]/div[1]/div[1]/div[2]/div').extract()[0]
        yield item





   


   
    



