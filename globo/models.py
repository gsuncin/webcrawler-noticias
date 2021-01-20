from django.db import models
from news_scrapy.settings import BASE_DIR


# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    link = models.URLField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to=BASE_DIR + '/media/')
    data = models.DateField()
    data_import = models.DateTimeField(auto_now_add=True)
