from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.account, name='account'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('wishlist', views.wishlist, name='wishlist'),
]
