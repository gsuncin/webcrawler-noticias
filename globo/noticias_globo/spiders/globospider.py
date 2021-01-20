import scrapy
# from globo.models import Noticia

class GlobospiderSpider(scrapy.Spider):
    name = 'globospider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia/']

    def parse(self, response):
        noticias = response.css('.bastian-page .bastian-feed-item')

        for noticia in noticias:
            titulo = noticia.css('.feed-post-link::text').extract_first()
            link = noticia.css('.feed-post-link::attr(href)').extract_first()
            descricao = noticia.css('.feed-post-body-resumo::text').extract_first()
            imagem = noticia.css('.feed-fd-picture-image::attr(src)').extract_first()
            data = noticia.css('.feed-post-datetime::text').extract_first()
            yield ({'titulo': titulo, 'link': link, 'descricao': descricao, 'imagem': imagem, 'data': data})

