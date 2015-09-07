from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tile, Collection, Group, PalleteColor, TileSize


@admin.register(Tile)
class TileAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es')
    search_fields = ['title', 'title_es']
    

@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es')
    search_fields = ['title', 'title_es']


@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es')
    search_fields = ['title', 'title_es']


@admin.register(PalleteColor)
class PalleteColorAdmin(admin.ModelAdmin):
	list_display = ('name', 'name_es')
	search_fields = ['name', 'name_es']


@admin.register(TileSize)
class TileSize(admin.ModelAdmin):
	pass