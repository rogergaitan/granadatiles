from django.contrib import admin
from apps.content.models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ImagesInline(admin.TabularInline):
	model = Images
	extra = 3
	verbose_name = "Images"


@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
	list_display = ('name', 'title', )
	inlines = [ImagesInline]
	readonly_fields = ('name',)
	fieldsets = (
		('General Info', {
			'fields': ('name', 'name_es', 'name_pr', 'title', 'title_es', 'title_pr', 'description', 'description_es', ),
			}),
		)