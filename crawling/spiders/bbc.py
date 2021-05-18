import scrapy
from crawling.items import NoticiaItem
from noticias.models import Noticia, Jornal


class BbcSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/portuguese/topics/c404v027pd4t/']

    def parse(self, response):
        noticias = response.xpath('//*[@id="lx-stream"]/div[1]/ol/li')
        for noticia in noticias:
            result = self.parse_item(noticia)
            yield result
        return len(noticias)

    def parse_item(self, response):
        i = NoticiaItem()
        i['titulo'] = response.xpath(".//h3/a/span/text()").extract_first()
        i['link'] = 'https://www.bbc.com/' + response.css(".qa-heading-link::attr(href)").extract_first()
        i['descricao'] = response.xpath(".//p/text()").extract()
        i['imagem'] = response.css(".qa-srcset-image::attr(src)").extract_first()
        i['jornal'] = "bbc"
        i.save()
        return
