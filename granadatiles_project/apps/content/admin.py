from django.contrib import admin
from apps.content.models import *
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

# Register your models here.


class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
	model = ImagesGroup
	extra = 3
	verbose_name = "Images"


@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
	list_display = ('name', 'title', )
	inlines = [ImagesInline]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
	model = Social
	list_display = ('name', 'link', 'order', 'active')


@admin.register(FeaturedVideo)
class VideoAdmin(SummernoteModelAdmin):
	list_display = ('title', 'title_es', )


@admin.register(CustomMessage)
class MessageCustomAdmin(SummernoteModelAdmin):
	list_display = ('name',  'title', )


@admin.register(Area)
class AreaAdmin(SummernoteModelAdmin):
	list_display = ('title', )



