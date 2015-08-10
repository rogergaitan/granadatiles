from django.contrib import admin
from apps.galleries.models import Gallery, GalleryOptions, GalleyImages

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ['title']
	search_fields = ['title']


class GalleryOptionsAdmin(admin.ModelAdmin):
	list_display = ('title', 'gallery')
	list_filter = ['title']
	search_fields = ['title']


class Carousel(admin.ModelAdmin):
	list_display = ('title', 'gallery_options')
	list_filter = ['title']
	search_fields = ['title']

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryOptions, GalleryOptionsAdmin)
admin.site.register(GalleyImages, Carousel)

