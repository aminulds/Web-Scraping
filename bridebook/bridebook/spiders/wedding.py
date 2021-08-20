# -*- coding: utf-8 -*-
import string
import scrapy
from scrapy import Request


class WeddingSpider(scrapy.Spider):
    name = 'wedding'
    allowed_domains = ['bridebook.co.uk']
    start_urls = ['https://bridebook.co.uk/search/wedding-venues/england']

    def parse(self, response):
        rows = response.xpath("//div[@class='bb-a bb-j bb-c bb-fv bb-ir bb-kp bb-cq bb-kt bb-ku']/div")

        for row in rows:
            item_url = row.xpath(".//a[2][@class='bb-dm bb-j bb-c bb-k bb-ls bb-ai bb-fw bb-ev bb-ic bb-hu bb-id bb-hw bb-ie']/@href").get()
            yield{
                'Link': response.urljoin(item_url),
                'Title': row.xpath(".//a[2]/div/div/div/div[@class='bb-eb bb-b bb-c bb-ec bb-ed bb-ee bb-ef bb-eg bb-du bb-mp bb-eh bb-mq']/text()").get(),
                'Price': row.xpath(".//a[2]/div/div[1]/div[2]/div[3]/div[2]/text()").get(),
                'Description': row.xpath(".//div/div[1]/div[4]/div[1]/text()").get()
            }

    
        next_urls = response.xpath("//div[@id='search-list-results']/div[2]/div//li/a/@href").extract()
        for next_url in next_urls:
            yield Request(next_url, callback=self.parse)
            
