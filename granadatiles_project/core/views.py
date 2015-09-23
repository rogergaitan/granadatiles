from rest_framework import viewsets
from django.conf import settings
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

class BaseViewSet(viewsets.ViewSet):

    def response(self, data, serializer):
        if data:
            return Response(serializer.data)
        else:
            return Response({}, status=HTTP_404_NOT_FOUND)

    def get_language(self, request):
        language = request.META.get('HTTP_X_LANGUAGE_CODE')
        return language
        