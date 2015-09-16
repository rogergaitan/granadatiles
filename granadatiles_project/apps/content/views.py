from django.shortcuts import render
from rest_framework.response import Response
from apps.content.serializers import TestimonySerializer, SectionSerializer
from apps.content.services import TestimonyService, SectionService
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
	
class SectionViewSet(BaseViewSet):
    def list(self, request):
        sections = SectionService.get_sections(
			language=self.get_language(request))
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)