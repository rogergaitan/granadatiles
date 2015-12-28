from django.db import models

class SectionManager(models.Manager):

    def get_seo_data(self, section_id, language):
        section = self.get(pk=section_id)
        data = {
            'title': section.get_page_title(language),
            'meta_description': section.meta_description,
            'meta_description_es': section.meta_description_es,
            'meta_keywords': section.meta_keywords,
            'meta_keywords_es': section.meta_keywords_es
        }
        return data
