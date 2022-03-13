from django.shortcuts import render
from .models import *


def index(request):
    context = {'title': 'Main'}

    return render(request,
                  'main/index.html',
                  context)


def price_list(request):
    context = {'title': 'Price-list'}

    return render(request,
                  'main/price-list.html',
                  context)


def contacts(request):
    context = {'title': 'Contacts'}

    return render(request,
                  'main/contacts.html',
                  context)


def portfolio(request):
    pictures = PortfolioPicture.objects.all()

    if request.method == 'GET':
        if 'search' in request.GET and request.GET['search'] != '':
            pictures_id = []
            search_words = request.GET['search'].lower().split()
            for picture in pictures:
                for search_word in search_words:
                    if picture.name.lower().find(search_word) != -1:
                        pictures_id.append(picture.id)
            pictures = PortfolioPicture.objects.filter(id__in=pictures_id)
    context = {'title': 'Портфолио',
               'pictures': pictures}

    return render(request,
                  'main/portfolio.html',
                  context)


def shop(request):
    pictures = ShopPicture.objects.all()

    if request.method == 'GET':
        if 'search' in request.GET and request.GET['search'] != '':
            pictures_id = []
            search_words = request.GET['search'].lower().split()
            for picture in pictures:
                for search_word in search_words:
                    if picture.name.lower().find(search_word) != -1:
                        pictures_id.append(picture.id)
            pictures = ShopPicture.objects.filter(id__in=pictures_id)

    context = {'title': 'Магазин',
               'pictures': pictures}

    return render(request,
                  'main/shop.html',
                  context)
