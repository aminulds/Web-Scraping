# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from book_scrape.items import BookScrapeItem

class BookSpider(scrapy.Spider):
    name = 'book'

    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        articles = response.xpath("//article[@class='product_pod']")

        for article in articles:
            loader = ItemLoader(item=BookScrapeItem(), selector=article)
            relative_url = article.xpath(".//div[@class='image_container']/a/img/@src").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('image_urls', absolute_url)
            loader.add_xpath('book_name', './/h3/a/@title')
            yield loader.load_item()

    
