from django.conf.urls import patterns, url
from apps.cart.views import cart_home, checkout_home

urlpatterns = [
    url(r'^$', cart_home, name='sr-home') ,
    url(r'^checkout$', checkout_home, name='sr-checkout')
]
