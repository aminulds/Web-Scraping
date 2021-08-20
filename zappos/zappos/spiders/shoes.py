# -*- coding: utf-8 -*-
import scrapy


class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['www.zappos.com']
    start_urls = ['https://www.zappos.com/men-running-shoes']

    def parse(self, response):
        for product in response.xpath("//article"):
            yield{
                'Name': product.xpath(".//p[@class='ag']/text()").get(),
                'Brand': product.xpath(".//p[@class='_f']/span/text()").get(),
                'Price': product.xpath(".//p/span[@class='jg kg' or @class='jg']/text()").get(),
                'Rating': product.xpath(".//p/span[@itemprop='aggregateRating']/@data-star-rating").get(),
                'Product_URL': response.urljoin(product.xpath(".//a[@class='bg']/@href").get())

            }

        next_page = response.xpath("//a[@class='uw']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
