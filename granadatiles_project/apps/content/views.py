﻿from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from apps.content.serializers import TestimonySerializer, SectionSerializer, SocialSerializer
from apps.content.services import TestimonyService, SectionService
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
	

class SocialViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Social.objects.exclude(url='')
    serializer_class = SocialSerializer