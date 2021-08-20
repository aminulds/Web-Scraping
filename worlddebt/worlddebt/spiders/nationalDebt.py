# -*- coding: utf-8 -*-
import scrapy


class NationaldebtSpider(scrapy.Spider):
    name = 'nationalDebt'
    allowed_domains = ['www.worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            country_name = row.xpath(".//td[1]/a/text()").get()
            gdp_debt = row.xpath(".//td[2]/text()").get()
            population = row.xpath(".//td[3]/text()").get()

            yield{
                'Country_name': country_name,
                'Gdp_Debt': gdp_debt,
                'Population': population
            }