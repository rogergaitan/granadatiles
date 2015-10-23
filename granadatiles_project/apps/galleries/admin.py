from django.contrib import admin
from apps.galleries.models import Gallery, GalleryImage, GalleryCategory, Designer, Photographer
from django_summernote.admin import SummernoteInlineModelAdmin


class ImagesInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = GalleryImage
    extra = 3
    verbose_name = "Images"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es', 'categories_count')
    search_fields = ['name', 'name_es']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es', 'images_count',  'gallery')
    inlines = [ImagesInline]
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    pass

@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    pass
