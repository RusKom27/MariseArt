from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('price-list', views.price_list, name='price-list'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('shop', views.shop, name='shop'),
]

