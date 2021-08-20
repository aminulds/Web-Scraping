# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WeddingVenuesSpider(CrawlSpider):
    name = 'wedding_venues'
    allowed_domains = ['bridebook.co.uk']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://bridebook.co.uk/search/wedding-venues/england', headers={
            'User_Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//a[@class='bb-dm bb-j bb-c bb-k bb-ls bb-ai bb-fw bb-ev bb-ic bb-hu bb-id bb-hw bb-ie'][2]"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(
            restrict_xpaths="//li[@class='next']/a"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User_Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield{
            'Venue_Name': response.xpath("//h1[@class='bb-a bb-b bb-c bb-e bb-dl bb-dp bb-ld bb-le bb-cu bb-ku bb-lf bb-lg bb-lh bb-li bb-lj bb-lk bb-ll bb-dr bb-ds bb-dt bb-lm']/text()").get(),
            'Bedroom': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[7]/div[2]/div/text()").get(),
            'Minimum_Price': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[1]/div[2]/div/text()").get(),
            'Maximum_Price': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[2]/div[2]/div/text()").get(),
            'Guest_Include': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[3]/div[2]/div/text()").get(),
            'Venue_Type': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[4]/div[2]/div/text()").get(),
            'Dining_Capacity': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[5]/div[2]/div/text()").get(),
            'Reciption_Capacity': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[6]/div[2]/div/text()").get(),
            'Stablished': response.xpath("(//div[@class='bb-a bb-j bb-c bb-k bb-l bb-cu'])[12]/div[2]/div/text()").get()

        }