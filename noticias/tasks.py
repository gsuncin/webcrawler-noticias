# Create your tasks here

from celery import shared_task
from noticias.models import Noticia


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Noticia.objects.count()
