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
		basecontentDto = [BaseContentDto(section, language=language)
			        for section in sections]
		return basecontentDto
	