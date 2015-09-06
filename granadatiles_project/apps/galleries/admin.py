from django.contrib import admin
from apps.galleries.models import Gallery, GalleryImage, GalleryCategory

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    list_filter = ['name']
    search_fields = ['name']

@admin.register(GalleryImage)
class GalleryImage(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ['title']
    search_fields = ['title']


