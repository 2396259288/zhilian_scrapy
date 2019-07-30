
import scrapy

from scrapy_splash import SplashRequest


class TbtaobaoSpider(scrapy.Spider):
    name = "av"
    # allowed_domains = ["www.taobao.com"]
    start_urls = ['https://www.bilibili.com/video/av17898771']

    def start_requests(self):
        for url in self.start_urls:
            # yield Request(url,dont_filter=True)
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        f = open('D:/av.html', 'w', encoding = 'utf-8')
        f.writelines(response.text)
        f.close()

        # print(response.text)
        # print(type(response.text))