import scrapy
from crawling.items import NoticiaItem
from scrapy.spiders import CrawlSpider
from noticias.models import Noticia, Jornal


class GlobospiderSpider(scrapy.Spider):
    name = 'globospider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia/']

    def parse(self, response, **kwargs):
        noticias = response.css('.bastian-page .bastian-feed-item')

        for row in noticias:
            yield self.parse_item(row)
        return len(noticias)

    def parse_item(self, response):
        i = NoticiaItem()
        i['titulo'] = response.css('.feed-post-link::text').extract_first()
        i['link'] = response.css('.feed-post-link::attr(href)').extract_first()
        i['descricao'] = response.css('.feed-post-body-resumo::text').extract_first()
        i['imagem'] = response.css('.bstn-fd-picture-image::attr(src)').extract_first().split()[0]
        i['jornal'] = "globo"
        i.save()
        return
