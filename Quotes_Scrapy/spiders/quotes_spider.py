# filename:quotes_spider.py
# author:Shao

import scrapy
from ..items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        quotes = QuotesItem()
        for quote in response.css('div.quote'):
            texts = quote.css('span.text::text').extract()
            authors = quote.css('small.author::text').extract()
            for text,author in zip(texts, authors):
                quotes['title'] = text
                quotes['author'] = author
                yield quotes
#                print quotes['title']

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)