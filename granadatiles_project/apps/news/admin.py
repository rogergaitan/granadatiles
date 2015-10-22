from django.contrib import admin
from .models import Catalog, Magazine, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'title_es' , 'url', 'date', 'magazine')
    search_fields = ['title', 'title_es']
    list_filter = ['magazine','date']


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('name', 'articles_count')
    search_fields = ['name']


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es')
    search_fields = ['name', 'name_es']
