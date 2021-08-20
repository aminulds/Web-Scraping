# -*- coding: utf-8 -*-
import scrapy


class BestsellerSpider(scrapy.Spider):
    name = 'bestseller'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='prlist row']/div"):
            yield{
                'Product_URL': product.xpath(".//div[@class='pimg default-image-front']/a/@href").get(),
                'Image_URL': product.xpath(".//div[@class='pimg default-image-front']/a/img[1]/@src").get(),
                'Name': product.xpath(".//a[@class='pull-left']/text()").get(),
                'Price': product.xpath(".//span[@class='pull-right']/text()").get()
            }
        
        next_pages = response.xpath("(//a[@class='page-link'])[4]/@href").get()
        if next_pages:
            yield response.follow(next_pages, callback=self.parse)
