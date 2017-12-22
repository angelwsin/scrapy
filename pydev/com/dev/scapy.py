
'''

默认的配置模块
1.配置初始化
__init__.Settings.__init__ 进行初始化操作
default_settings

---crawler.Crawler爬虫者
配置中加载 SPIDER_LOADER_CLASS = 'scrapy.spiderloader.SpiderLoader'
 --主要逻辑 crawler.Crawler.crawl
ExecutionEngine
 --SCHEDULER = 'scrapy.core.scheduler.Scheduler'
 --DOWNLOADER = 'scrapy.core.downloader.Downloader'
    --DOWNLOAD_HANDLERS
 --spider--继承scrapy.Spider 
 __init__.Spider.start_requests
    --start_urls 封装到 Request
    
--reactor.CallLaterOnce 中处理请求
      --engine.ExecutionEngine._next_request
      --engine.ExecutionEngine._next_request_from_scheduler 真正的处理请求
 --down下载 __init__.Downloader.fetch
    链式处理-------- 组件
    DOWNLOADER_MIDDLEWARES_BASE = {
    # Engine side
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
    # Downloader side
}

SPIDER_MIDDLEWARES--

'''
import scrapy
from scrapy.crawler import CrawlerProcess


class XSpider(scrapy.Spider):
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

process.crawl(XSpider)
process.start() # the script will block here until the crawling is finished