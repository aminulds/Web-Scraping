# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/index.html', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='image_container']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent']= self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'Book Name': response.xpath("//h1/text()").get(),
            'Book Price': response.xpath("//p[@class='price_color']/text()").get(),
            'URL': response.url,
            # 'User-Agent': response.request.headers['User-Agent']
            'Description': response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        }
