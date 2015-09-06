from django.contrib import admin
from .models import Catalog, Magazine, Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title',)

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    search_fields = ['name', 'name_es']
