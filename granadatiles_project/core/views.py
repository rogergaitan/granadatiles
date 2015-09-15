from rest_framework import viewsets
from django.conf import settings

class BaseViewSet(viewsets.ViewSet):

    def get_language(self, request):
        language = request.META.get('HTTP_X_LANGUAGE_CODE')
        return language
        