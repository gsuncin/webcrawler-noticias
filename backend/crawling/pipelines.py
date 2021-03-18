# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from noticias.models import Noticia


class CrawlingPipeline:
    def process_item(self, item, spider):
        Noticia.objects.create(
            titulo=item['titulo'],
            link=item['link'],
            descricao=item['descricao'],
            imagem=item['imagem'],
        )
        return item
