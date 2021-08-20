# -*- coding: utf-8 -*-
import scrapy


class SlickSpider(scrapy.Spider):
    name = 'slick'
    allowed_domains = ['slickdeals.net']
    start_urls = ['https://slickdeals.net/deal-categories']

    def parse(self, response):
        category_id = 0
        for category in response.xpath("////ul[@class='featured-deals']/li"):
            category_link = response.urljoin(category.xpath(".//a/@href").get())
            category_id +=1
            yield response.follow(category_link, callback=self.product_parse, meta={'category_id': category_id})
         
    def product_parse(self, response):
        category_id =response.request.meta['category_id']

        for product in response.xpath("//ul[@class='dealTiles categoryGridDeals']/li"):
            link= product.xpath(".//a[@class='itemTitle bp-c-link']/@href").get()
            ab_link = f"https://slickdeals.net{link}"

            yield{
                'Category': category_id,
                'URL': ab_link,
                'Name': product.xpath(".//a[@class='itemTitle bp-c-link']/text()").get(),
                'Store Name': product.xpath(".//span[@class='itemStore']/text()").get().strip(),
                'Price': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get()
            }

        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            ab_url = f"https://slickdeals.net{next_page}"
            yield response.follow(ab_url, callback=self.product_parse, meta={'category_id': category_id})