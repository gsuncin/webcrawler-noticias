import scrapy


class NoticiasSpider(scrapy.Spider):
    nome = 'noticias'

    start_urls = ['https://https://www.uol.com.br/']
