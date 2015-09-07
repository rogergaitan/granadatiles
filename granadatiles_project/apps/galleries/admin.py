from django.contrib import admin
from apps.galleries.models import Gallery, GalleryImage, GalleryCategory
from django_summernote.admin import SummernoteInlineModelAdmin


class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = GalleryImage
    extra = 3
    verbose_name = "Images"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    inlines = [ImagesInline]
    list_filter = ['name']
    search_fields = ['name']
