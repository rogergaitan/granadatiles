from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from apps.content.serializers import TestimonySerializer, SectionSerializer, SocialSerializer, SectionCoverSerializer, FeaturedVideoSerializer
from apps.content.services import TestimonyService, SectionService, FeaturedVideoService
from .models import Social
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
	
    
    def retrieve(self, request, pk=None):
        section = SectionService.get_section(
            id=pk, 
            language=self.get_language(request))
        serializer = SectionSerializer(section)
        return Response(serializer.data)
	
	
    @detail_route(methods=['get'])
    def cover(self, request, pk=None):
        cover = SectionService.get_cover(section_id=pk)
        serializer = SectionCoverSerializer(cover)
        return Response(serializer.data)
	

class SocialViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Social.objects.exclude(url='')
    serializer_class = SocialSerializer
    

class FeaturedVideoViewSet(BaseViewSet):
    def list(self, request):
        videos = FeaturedVideoService.get_videos(language=self.get_language(request))
        serializer = FeaturedVideoSerializer(videos, many=True)
        return Response(serializer.data)