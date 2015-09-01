from django.contrib import admin
from apps.content.models import *
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

# Register your models here.


class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
	model = Images
	extra = 3
	verbose_name = "Images"


@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
	list_display = ('name', 'title', )
	inlines = [ImagesInline]
	fieldsets = (
		('General Info', {
			'fields': ('name', 'name_es', 'title', 'title_es', 'description', 'description_es', ),
			}),
		)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
	model = Social
	list_display = ('name', 'link', 'order', 'active')


@admin.register(FeaturedVideo)
class VideoAdmin(SummernoteModelAdmin):
	list_display = ('title', 'title_es', )
	fieldsets = (
		('General Info', {
			'fields': ('title', 'title_es', 'video', ),
		}),
	)


@admin.register(CustomMessage)
class MessageCustomAdmin(SummernoteModelAdmin):
	list_display = ('name',  'title', )
	fieldsets = (
		('General Info', {
			'fields': ('name', 'name_es', 'title', 'title_es', 'description', 'description_es', ),
		}),
	)


@admin.register(Area)
class AreaAdmin(SummernoteModelAdmin):
	list_display = ('title', )
	fieldsets = (
		('General Info', {
			'fields': ('title', 'title_es', 'message', 'message_es',),
			})
		),



