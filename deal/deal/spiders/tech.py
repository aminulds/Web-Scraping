# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class TechSpider(scrapy.Spider):
    name = 'tech'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/deals/tech',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        for product in response.xpath("//ul[@class='dealTiles categoryGridDeals']/li"):
            yield{
                'name': product.xpath(".//a[@class='itemTitle bp-c-link']/text()").get(),
                'p_link': response.urljoin(product.xpath(".//a[@class='itemTitle bp-c-link']/@href").get()),
                'price': product.xpath("normalize-space(.//div[@class='itemPrice  wide ']/text())").get(),
                'store_name': product.xpath("normalize-space(.//button[@data-no-linkable='data-no-linkable']/text())").get(),
            }

        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            absolute_url = f"https://slickdeals.net{next_page}"
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )