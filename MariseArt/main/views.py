from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .decorators import *


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


@unauthenticated_user
def auth(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        elif 'register' in request.POST:
            form = CustomUserCreationForm(request.POST)
            user = form.save()
            login(request, user)
            return redirect('home')
    context = {'title': 'Auth',
               'form': form}

    return render(request,
                  'main/auth.html',
                  context)


@login_required(login_url='auth')
def unauth(request):
    logout(request)
    return redirect('auth')


@login_required(login_url='login')
def portfolio(request):
    pictures = PortfolioPicture.objects.all()

    if request.method == 'GET':
        if 'search' in request.GET and request.GET['search'] != '':
            pictures_id = []
            search_words = request.GET['search'].lower().split()
            for picture in pictures:
                for search_word in search_words:
                    if picture.picture.name.lower().find(search_word) != -1:
                        pictures_id.append(picture.id)
            pictures = PortfolioPicture.objects.filter(id__in=pictures_id)
    context = {'title': 'Портфолио',
               'pictures': pictures}

    return render(request,
                  'main/portfolio.html',
                  context)


@login_required(login_url='login')
def shop(request):
    pictures = ShopPicture.objects.all()

    if request.method == 'GET':
        if 'search' in request.GET and request.GET['search'] != '':
            pictures_id = []
            search_words = request.GET['search'].lower().split()
            for picture in pictures:
                for search_word in search_words:
                    if picture.picture.name.lower().find(search_word) != -1:
                        pictures_id.append(picture.id)
            pictures = ShopPicture.objects.filter(id__in=pictures_id)

    context = {'title': 'Магазин',
               'pictures': pictures}

    return render(request,
                  'main/shop.html',
                  context)
