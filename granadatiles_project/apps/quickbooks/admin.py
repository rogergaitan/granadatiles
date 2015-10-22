from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'quantity_on_hand','sales_price', 'sublevel', 'is_active')
    list_filter = ('is_active', 'sublevel')
    search_fields = ('full_name', 'name')
