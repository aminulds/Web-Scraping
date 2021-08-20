# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GirlsSpider(CrawlSpider):
    name = 'girls'
    allowed_domains = ['www.zappos.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.zappos.com/girls', headers={
            'User-Agent': self.user_agent
        }) 

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="bg"]'), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="uw"]'), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent']= self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'Brand': response.xpath("//a/span[@itemprop='name']/text()").get(),
            'Name': response.xpath("//span[@class='ft']/text()").get(),
            'Price': response.xpath("(//span[@class='qq'])[2]/text()").get(),
            'Shiping': response.xpath("//span[@class='kn']/text()").get(),
            'Rating': response.xpath("//span[@class='nj Ts']/@data-star-rating").get(),
            'URL': response.url,
            'User_Agent': response.request.headers['User-Agent']
        }
        
