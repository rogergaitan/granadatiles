from django.contrib import admin
from .models import Catalog, Magazine, Video, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
	model = Article
	list_display = ('name',)


class MagazineAdmin(admin.ModelAdmin):
	list_display = ('title', 'name', 'url')
	list_filter = ['date']
	search_fields = ['title']


class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'youtube_url_format')
	search_fields = ['title']


class CatalogAdmin(admin.ModelAdmin):
	list_display = ('title', 'title_es')
	search_fields = ['title', 'title_es']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Video, VideoAdmin)
