# -*- coding: utf-8 -*-
import string
import scrapy
from scrapy import Request


class MymangaSpider(scrapy.Spider):
    name = 'mymanga'
    start_urls = ['https://myanimelist.net/manga.php']

    def parse(self, response):
        abc_page = "//div[@id='horiznav_nav']//li/a/@href"
        return(Request(url, callback=self.parse_list_page) for url in response.xpath(abc_page).extract())

    def parse_list_page(self, response):
        rows = response.css("div.js-categories-seasonal tr ~ tr")
        for row in rows:
            yield{
                "title":  row.css('a[id] strong::text').get(),
                "synopsis": row.css("div.pt4::text").get(),
                "type_": row.css('td:nth-child(3)::text').get().strip(),
                "episodes": row.css('td:nth-child(4)::text').get().strip(), 
                "rating": row.css('td:nth-child(5)::text').get().strip(),
            }
        
        next_urls = response.xpath("//div[@class='spaceit']//a/@href").extract()
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse_list_page)

