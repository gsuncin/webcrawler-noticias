from django.shortcuts import render


def index(request):
    context = {
        "null": 'null'
    }
    return render('index.html', context)
