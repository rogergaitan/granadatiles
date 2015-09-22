import random
from .models import Testimony, Section
from .dtos import TestimonyDto, SectionCoverDto
from apps.news.models import Article
from apps.news.dtos import ArticleDto
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
        ids = section.images.values_list('id')
        choice = random.sample(list(ids), 1)
        image = section.images.get(pk=choice[0][0])
        return image
	
    def get_cover(section_id):
        section = Section.objects.get(pk=section_id)
        cover = SectionService.get_random_cover(section)
        sectioncoverDto = SectionCoverDto(cover)
        featured_article = ArticleDto(Article.objects.get(pk=cover.featured_article.id))
        sectioncoverDto.featuredArticle = featured_article
        return sectioncoverDto
	
    