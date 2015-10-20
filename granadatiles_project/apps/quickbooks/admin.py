from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'quantity_on_hand')
    list_filter = ('full_name',)
    search_fields = ('full_name',)
