# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/index.html')

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='image_container']/a"),
             callback='parse_item'),
        Rule(LinkExtractor(
            restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        yield{
            'Book Name': response.xpath("//h1/text()").get(),
            'Book Price': response.xpath("//p[@class='price_color']/text()").get(),
            'URL': response.url,
            'Description': response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        }
