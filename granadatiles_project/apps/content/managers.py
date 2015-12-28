from django.db import models

class SectionManager(models.Manager):

    def get_seo_data(self, section_id, language):
        section = self.get(pk=section_id)
        data = {
            'title': section.get_page_title(language),
            'meta_description': section.get_meta_description(language),
            'meta_keywords': section.get_meta_keywords(language)
        }
        return data
