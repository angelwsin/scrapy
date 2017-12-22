'''
Created on 2017年12月22日

@author: Administrator
'''
import re

import scrapy
from scrapy.crawler import CrawlerProcess


class XSpider(scrapy.Spider):
    # Your spider definition
    name = "address"
    start_urls = [
        'http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html',
    ]
    
    file  = open('E:/test.txt', 'w+')
    prov = re.compile(r'<p class="MsoNormal"><b><span lang="EN-US">(\d+)<span>     </span></span></b><b><span style="font-family: 宋体">(.*)</span></b></p>');
    city = re.compile(r'<p class="MsoNormal"><span style="font-family: 宋体">　</span><span lang="EN-US">(\d+)<span>         </span></span><span style="font-family: 宋体">　(.*)</span></p>')
    dist = re.compile(r'<p class="MsoNormal"><span style="font-family: 宋体">　　</span><span lang="EN-US">(\d+)<span>     </span></span><span style="font-family: 宋体">　　(.*)</span></p>')
    def parseSpan(self,span):
        match = self.prov.match(span)
        if match:
            self.file.write('prov '+match.group(1)+' '+match.group(2)+'\n')
        cy   = self.city.match(span)
        if cy :
            self.file.write('city '+cy.group(1)+' '+cy.group(2)+'\n')
        dt   = self.dist.match(span);
        if dt :
            self.file.write('dist '+dt.group(1)+' '+dt.group(2)+'\n')
           
    def parse(self, response):
        for quote in response.css('div.TRS_PreAppend'):
                for span in quote.xpath('p').extract():
                    self.parseSpan(span)
        self.file.close()        

        
   
    
    
    
      
        
    ...
'''
组件 配置 Settings
'''
process = CrawlerProcess({
    'FILES_STORE':'E:/test.txt','USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(XSpider)
process.start() # the script will block here until the crawling is finished