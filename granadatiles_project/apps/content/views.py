from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from apps.content.serializers import TestimonySerializer, SectionSerializer, SocialSerializer, SectionCoverSerializer, FeaturedVideoSerializer, IndexNavigationSerializer, FlatPageSerializer, FlatPageCoverSerializer, FlatPageMenuSerializer, CollectionContentSerializer
from apps.content.services import TestimonyService, SectionService, FeaturedVideoService, AreaService, IndexNavigationService, FlatPageService, CollectionContentService
from .models import Social, Section
from core.views import BaseViewSet
from core.serializers import BaseContentSerializer
from rest_framework.status import HTTP_404_NOT_FOUND
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import Http404, HttpResponsePermanentRedirect, HttpResponse
from django.contrib.flatpages.models import FlatPage
from django.utils.safestring import mark_safe
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from apps.content.models import ExtendedFlatPage

DEFAULT_TEMPLATE = 'flatpages/default.html'

def flatpage(request, url):
    if not url.startswith('/'):
        url = '/' + url
    site_id = get_current_site(request).id
    try:
        if request.LANGUAGE_CODE == 'es':
            f = get_object_or_404(ExtendedFlatPage,
            url_es=url, sites=site_id)
        else:
            f = get_object_or_404(FlatPage,
                url=url, sites=site_id)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            f = get_object_or_404(FlatPage,
                url=url, sites=site_id)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_flatpage(request, f)


@csrf_protect
def render_flatpage(request, f):
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template_name:
        template = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        template = loader.get_template(DEFAULT_TEMPLATE)

    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    response = HttpResponse(template.render({'flatpage': f}, request))
    return response


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

def search(request):
    return render(request, 'content/search.html')


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

class FlatPageViewSet(BaseViewSet):
    def list(self, request):
        menuid = request.query_params.get('menuId')
        flatPages = FlatPageService.get_flatpages_for_menu(menuid, 
                                                           language = self.get_language(request))
        serializer = FlatPageMenuSerializer(flatPages, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        flatPage = FlatPageService.get_flatpage(pk, 
                                                self.get_language(request))
        serializer = FlatPageSerializer(flatPage)
        return Response(serializer.data)
    
    @detail_route(methods=['get'])
    def cover(self, request, pk = None):
        cover = FlatPageService.get_cover(pk)
        serializer = FlatPageCoverSerializer(cover)
        return Response(serializer.data)

class CollectionContentViewSet(BaseViewSet):
    def list(self, request):
        collectionid = request.query_params.get('collectionId', 0)
        collectionContent = CollectionContentService.get_menu_content(collectionid,
                                                                 self.get_language(request))
        serializer = FlatPageMenuSerializer(collectionContent, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        collectionContent = CollectionContentService.get_content(pk, 
                                                self.get_language(request))
        serializer = CollectionContentSerializer(collectionContent)
        return Response(serializer.data)

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
