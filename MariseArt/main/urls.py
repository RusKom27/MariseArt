from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('price-list', views.price_list, name='price-list'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contacts', views.contacts, name='contacts'),
    path('auth', views.auth, name='auth'),
    path('unauth', views.unauth, name='unauth'),
    path('shop', views.shop, name='shop'),
]

