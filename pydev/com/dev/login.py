'''
Created on 2017年12月22日

@author: Administrator
'''
import scrapy
from scrapy.crawler import CrawlerProcess



class LoginSpider(scrapy.Spider):
    # Your spider definition
    name = "quotes"
    start_urls = [
        'https://tieba.baidu.com/index.html',
    ]

    def parse(self, response):
       
        for quote in response.css('img'):
            print(quote.xpath('@src').extract());

        
    pass
    ...

'''
组件 配置 Settings
'''
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(LoginSpider)
process.start() # the script will block here until the crawling is finished