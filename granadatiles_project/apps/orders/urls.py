from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import OrdersViewSet
                    

router = DefaultRouter()
router.register('orders', OrdersViewSet, base_name='orders')
urlpatterns = router.urls 
