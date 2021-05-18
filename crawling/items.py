# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from noticias.models import Noticia, Jornal


class NoticiaItem(DjangoItem):
    django_model = Noticia
    image_urls = scrapy.Field()
    images = scrapy.Field()
