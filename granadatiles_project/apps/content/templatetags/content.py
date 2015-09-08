from django import template
from apps.content.models import Section, Area, Social, FeaturedVideo
from django.conf import settings

register = template.Library()


@register.inclusion_tag('content/area.html')
def area(area_id, language):
	area = Area.objects.get(pk=area_id)
	return {
			'area':area.get_message(language)
		}


@register.inclusion_tag('content/carousel.html')
def carousel(section_id, language):
	images_query_set = Section.objects.get(id=section_id).carousel.all()
	images = []
	for image in images_query_set:
		images.append({
				'description': image.get_description(language),
				'url': image.image.url if image.image else '',
				'link': image.link if image.link else '',
				'action_text': image.get_action_text(language),
				'target': image.target
			})
	return{
			'images': images,
			'MEDIA_URL': settings.MEDIA_URL
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
	section = {'title': section_query_set.get_title(language), 'message': section_query_set.get_message(language)}
	return section