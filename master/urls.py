from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('medicinedetail/<int:id>/', medicinedetail, name='medicinedetail'),
    path('shop/', shop, name='shop'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/', cart, name='cart'),
    path('delusercart/<int:id>/', delusercart, name='delusercart'),
    path('checkout/', checkout, name='checkout'),
    path('profile/', Profile, name='Profile'),
    path('ordercomplete/', ordercomplete, name='ordercomplete'),
    path('Ordered/', ordered, name='ordered'),
    path('about/', about, name='about')
]
