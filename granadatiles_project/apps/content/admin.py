from django.contrib import admin
from apps.content.models import *
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = SectionImage
    extra = 3
    verbose_name = "Images"

@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
    list_display = ('name', 'title', )
    inlines = [ImagesInline]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('name', 'url', 'order', 'active')


@admin.register(FeaturedVideo)
class VideoAdmin(SummernoteModelAdmin):
    list_display = ('name', 'name', )


@admin.register(Area)
class AreaAdmin(SummernoteModelAdmin):
    list_display = ('title', )



