from django.contrib import admin

from .models import Order, OrderDetail, Address


class OrderDetailInline(admin.StackedInline):
    model = OrderDetail
    fields = ('tile', 'customized_tile', 'input_sq_ft', 'price_per_sq_ft',
              'price_per_tile', 'base_cost', 'box')


class AddressInline(admin.StackedInline):
    model = Address
    fields = ('street_building_house_line1', 'house_apt_line2', 
              'zipcode', 'province_state', 'city')
    extra = 2


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_first_name', 'customer_last_name', 'user')
    inlines = [AddressInline, OrderDetailInline]