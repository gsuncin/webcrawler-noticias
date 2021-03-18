import scrapy
from backend.crawling.items import NoticiaItem
from scrapy.spiders import CrawlSpider
from noticias.models import Noticia, Jornal



class GlobospiderSpider(scrapy.Spider):
    name = 'globospider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia/']

    def parse(self, response):
        noticias = response.css('.bastian-page .bastian-feed-item')
        noticiasxpath = response.xpath('//*[@id="feed-placeholder"]/div/div/div[2]/div/div/div/div[1]/div')

        for row in noticias:
            result = self.parse_item(row)
            yield result

    def parse_item(self, response):
        i = NoticiaItem()
        i['titulo'] = response.css('.feed-post-link::text').extract_first()
        i['link'] = response.css('.feed-post-link::attr(href)').extract_first()
        i['descricao'] = response.css('.feed-post-body-resumo::text').extract_first()
        i['imagem'] = response.css('.bstn-fd-picture-image::attr(src)').extract_first().split()[0]
        i['jornal'] = "Globo"
        return i
#\34 8fa6879969c9c96f77cd973daa90d8d > div > div.feed-media-wrapper > a