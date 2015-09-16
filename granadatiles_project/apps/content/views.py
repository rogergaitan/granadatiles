from django.shortcuts import render
from rest_framework.response import Response
from apps.content.serializers import TestimonySerializer
from apps.content.services import TestimonyService
from core.views import BaseViewSet


def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'content/about_us.html')


class TestimonyViewSet(BaseViewSet):
    # /testimonials
    def list(self, request):
        testimonials = TestimonyService.get_testimonials(
            language=self.get_language(request))
        serializer = TestimonySerializer(testimonials, many=True)
        return Response(serializer.data)