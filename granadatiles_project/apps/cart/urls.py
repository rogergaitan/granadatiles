from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register('cart', CartViewSet, base_name='cart')

urlpatterns = router.urls
