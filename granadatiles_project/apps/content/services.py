import random
from .models import Testimony, Section, FeaturedVideo
from .dtos import TestimonyDto, SectionCoverDto, FeaturedVideoDto
from apps.news.models import Article
from apps.news.dtos import  SectionFeaturedArticleDto
from core.dtos import BaseContentDto


class TestimonyService(object):
    def get_testimonials(language=None):
        testimonials = Testimony.objects.all()
        testimonialsDto = [TestimonyDto(testimony, language=language)
                           for testimony in testimonials]
        return testimonialsDto

class SectionService(object):
    def get_sections(language=None):
        sections = Section.objects.all()
        sectionsDto = [BaseContentDto(section, language=language)
			        for section in sections]
        return sectionsDto
	
    def get_section(id, language=None):
        section = Section.objects.get(pk=id)
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
        section = Section.objects.get(pk=section_id)
        cover = SectionService.get_random_cover(section)
        if cover:
            sectioncoverDto = SectionCoverDto(cover)
            if cover.featured_article:
                sectioncoverDto.featuredArticle = SectionFeaturedArticleDto(cover.featured_article, language)
            return sectioncoverDto
        else:
            return None
	

class FeaturedVideoService(object):
    def get_videos(language=None):
        videos = FeaturedVideo.objects.all()
        videosDto = [FeaturedVideoDto(video, language=language) for video in videos]
        return videosDto