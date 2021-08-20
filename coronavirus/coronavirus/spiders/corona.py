# -*- coding: utf-8 -*-
import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['www.worldometers.info/coronavirus']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            country = row.xpath(".//td[1]/text()").get()
            total_cases = row.xpath(".//td[2]/text()").get()
            new_cases = row.xpath(".//td[3]/text()").get()
            total_deaths = row.xpath(".//td[4]/text()").get()
            new_deaths = row.xpath(".//td[5]/text()").get()
            total_recover = row.xpath(".//td[6]/text()").get()
            serious = row.xpath(".//td[7]/text()").get()

            yield{
                'Country': country,
                'Total Cases': total_cases,
                'New Cases': new_cases,
                'Total Deaths': total_deaths,
                'New Deaths': new_deaths,
                'Total Recover': total_recover,
                'Serious': serious
            }