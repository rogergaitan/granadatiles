from apps.content.models import Testimony, Section
from apps.content.dtos import TestimonyDto
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
        sectionDto = BaseContentDto(section, language)  
        return sectionDto