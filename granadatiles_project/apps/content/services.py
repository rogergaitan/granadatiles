﻿import random
from django.shortcuts import get_object_or_404
from .models import Testimony, Section, FeaturedVideo, Area
from .dtos import TestimonyDto, SectionCoverDto, FeaturedVideoDto
from apps.news.models import Article
from apps.news.dtos import  SectionFeaturedArticleDto, ArticleMagazineDto
from core.dtos import BaseContentDto
from apps.content.models import IndexNavigation, ExtendedFlatPage, CollectionContent
from apps.content.dtos import IndexNavigationDto, FlatPageDto, FlatPageCoverDto, FlatPageMenuDto, CollectionContentDto


class TestimonyService(object):
    def get_testimonials(language=None):
        testimonials = Testimony.objects.all()
        testimonialsDto = [TestimonyDto(testimony, language=language)
                           for testimony in testimonials]
        return testimonialsDto


class SectionService(object):
    def get_sections(language=None):
        sections = Section.objects.all()
        sectionsDto = [BaseContentDto(section, language=language) for section in sections]
        return sectionsDto

    def get_section(id, language=None):
        section = get_object_or_404(Section, pk=id)
        sectionDto = BaseContentDto(section, language=language)
        return sectionDto

    def get_random_cover(section):
        if section.images.all().count() > 0:
            ids = section.images.values_list('id')
            choice = random.sample(list(ids), 1)
            image = section.images.get(pk=choice[0][0])
            return image
        else:
            return None

    def get_cover(section_id, language):
        section = get_object_or_404(Section, pk=section_id)
        cover = SectionService.get_random_cover(section)
        if cover:
            sectioncoverDto = SectionCoverDto(cover, language)
            if cover.featured_article:
                sectioncoverDto.featuredArticle = SectionFeaturedArticleDto(cover.featured_article, language)
            if cover.articles.count() > 0:
                sectioncoverDto.articles = [ArticleMagazineDto(article) for article in cover.articles.all()]
            return sectioncoverDto
        else:
            return None

class FlatPageService(object):

    def get_flatpages_for_menu(menuId , language=None):
        flatpages = ExtendedFlatPage.objects.filter(menu=int(menuId))
        flatpagesDto = [FlatPageMenuDto(flatpage, language) for flatpage in flatpages]
        return flatpagesDto

    def get_flatpage(title, language=None):
        flatpage = get_object_or_404(ExtendedFlatPage, title=title)
        flatPageDto = FlatPageDto(flatpage, language = language)
        return flatPageDto

    def get_cover(title):
       flatPage = get_object_or_404(ExtendedFlatPage, title=title)
       flatPageCoverDto = FlatPageCoverDto(flatPage)
       return flatPageCoverDto

class CollectionContentService(object):

    def get_menu_content(collectionId, language=None):
        content = CollectionContent.objects.filter(collection__id = collectionId)
        contentDto = [FlatPageMenuDto(item, language) for item in content]
        return contentDto

    def get_content(title, language=None):
        content = get_object_or_404(CollectionContent, title=title)
        collectionContentDto = CollectionContentDto(content, language=language)
        return collectionContentDto

class FeaturedVideoService(object):

    def get_videos(language=None):
        videos = FeaturedVideo.objects.all()
        videosDto = [FeaturedVideoDto(video, language=language) for video in videos]
        return videosDto


class AreaService(object):

    def get_area(id, language=None):
        area = get_object_or_404(Area,pk=id)
        areaDto = BaseContentDto(area, language)
        return areaDto

class IndexNavigationService(object):

    def get_index_navigation(language=None):
        index_navigation_objects = IndexNavigation.objects.all()
        index_navigation_dto = [IndexNavigationDto(index_object, language=language) for index_object in index_navigation_objects]
        return index_navigation_dto
