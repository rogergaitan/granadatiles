from django.conf.urls import patterns, url
from apps.cart.views import cart_home

urlpatterns = [
    url(r'^$', cart_home, name='sr-home')
]
