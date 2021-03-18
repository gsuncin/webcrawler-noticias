import scrapy
from backend.crawling.items import NoticiaItem
from scrapy.spiders import CrawlSpider



class GlobospiderSpider(CrawlSpider):
    name = 'globospider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia/']

    def parse(self, response):
        noticias = response.css('.bastian-page .bastian-feed-item')
        print(noticias)
        for row in noticias:
            print(row)
            link = 'https://g1.globo.com/economia/tecnologia/' + row
            yield scrapy.Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        i = NoticiaItem()
        i['titulo'] = response.css('.feed-post-link::text').extract_first()
        i['link'] = response.css('.feed-post-link::attr(href)').extract_first()
        i['descricao'] = response.css('.feed-post-body-resumo::text').extract_first()
        i['imagem'] = response.css('.feed-fd-picture-image::attr(src)').extract_first()
        i['data'] = response.css('.feed-post-datetime::text').extract_first()
        return i

