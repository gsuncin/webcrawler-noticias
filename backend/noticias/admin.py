from django.contrib import admin
from .models import Noticia, Jornal


class NoticiaAdmin(admin.ModelAdmin):
    class Meta:
        list_fields = ['titulo', 'link', 'descricao', 'imagem', 'data', 'data_import']


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Jornal)
