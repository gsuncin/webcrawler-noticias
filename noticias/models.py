from django.db import models


class Jornal(models.Model):
    nome = models.CharField(max_length=255, null=False)
    slug = models.SlugField()


class Noticia(models.Model):
    titulo = models.CharField(max_length=500, null=False)
    link = models.URLField()
    descricao = models.TextField()
    imagem = models.URLField()
    data_import = models.DateTimeField(auto_now_add=True)
    jornal = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
