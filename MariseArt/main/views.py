from django.shortcuts import render


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


def portfolio(request):
    context = {'title': 'Portfolio'}

    return render(request,
                  'main/portfolio.html',
                  context)

