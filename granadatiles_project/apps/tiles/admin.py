from django.contrib import admin
from .models import Tile, Collection, Group

class TileAdmin(admin.ModelAdmin):
    pass

class CollectionAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tile, TileAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Group, GroupAdmin)