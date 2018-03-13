from django import template
from apps.content.models import Section, Area, Social, FeaturedVideo, ExtendedFlatPage, CollectionContent
from django.conf import settings

register = template.Library()


@register.inclusion_tag('content/area.html')
def area(area_id, language):
    area = Area.objects.get(pk=area_id)
    return {
            'area':area.get_message(language)
        }

@register.inclusion_tag('content/social_media.html')
def social():
    social = Social.objects.filter(active=True).order_by('order')
    return {
        'social': social,
    }


@register.inclusion_tag('content/video.html')
def video(video_id, language):
    video = FeaturedVideo.objects.get(pk=video_id)
    return {
            'title':video.get_title(language),
            'video':video.video,
        }

@register.assignment_tag()
def section(section_id, language):
    section_query_set = Section.objects.get(id=section_id)
    seo_data = format_seo_data(language, section_query_set)
    return seo_data

@register.assignment_tag()
def extendedflatpage(extendedFlatPageId, language):
    flatpage_query_set = ExtendedFlatPage.objects.get(id=extendedFlatPageId)
    seo_data = format_seo_data(language, flatpage_query_set)
    return seo_data

@register.assignment_tag()
def collectioncontent(collectionContentId, language):
    collectioncontent_query_set = CollectionContent.objects.get(id=collectionContentId)
    seo_data = format_seo_data(language, collectioncontent_query_set)
    return seo_data

@register.inclusion_tag('content/meta.html')
def content_meta_tags(section):
    return {
            'section': section
        }

def format_seo_data(language, section_query_set):
    section = {
        'page_title': section_query_set.get_page_title(language),
        'meta_description_es': section_query_set.meta_description_es,
        'meta_description': section_query_set.meta_description,
        'meta_keywords_es': section_query_set.meta_keywords_es,
        'meta_keywords': section_query_set.meta_keywords,
        }
    return section