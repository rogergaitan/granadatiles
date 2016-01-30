from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from apps.content.serializers import TestimonySerializer, SectionSerializer, SocialSerializer, SectionCoverSerializer, FeaturedVideoSerializer, IndexNavigationSerializer
from apps.content.services import TestimonyService, SectionService, FeaturedVideoService, AreaService, IndexNavigationService
from .models import Social, Section
from core.views import BaseViewSet
from core.serializers import BaseContentSerializer
from rest_framework.status import HTTP_404_NOT_FOUND


def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'content/about_us.html')


def videos(request):
    return render(request, 'content/featured_videos.html')


def compare_products(request):
    return render(request, 'content/compare_products.html')

def cement_vs_ceramic(request):
    return render(request, 'content/cement_vs_ceramic.html')

def color_palletes(request):
    return render(request, 'content/color_palletes.html')


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
        cover = SectionService.get_cover(section_id=pk,
                                         language=self.get_language(request))
        serializer = SectionCoverSerializer(cover)
        return self.response(cover, serializer)


class SocialViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Social.objects.exclude(url='')
    serializer_class = SocialSerializer


class FeaturedVideoViewSet(BaseViewSet):

    def list(self, request):
        videos = FeaturedVideoService.get_videos(language=self.get_language(request))
        serializer = FeaturedVideoSerializer(videos, many=True)
        return Response(serializer.data)

class AreaViewSet(BaseViewSet):

    def retrieve(self, request, pk=None):
        area = AreaService.get_area(id=pk, language=self.get_language(request))
        serializer = BaseContentSerializer(area)
        return Response(serializer.data)


class IndexNavigationViewSet(BaseViewSet):

    def list(self, request):
        index_navigation = IndexNavigationService.get_index_navigation(language=self.get_language(request))
        serialize = IndexNavigationSerializer(index_navigation, many=True)
        return Response(serialize.data)
