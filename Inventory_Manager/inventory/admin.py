from django.contrib import admin
from .models import Warehouse, Product, Stock, Supply, SuppliedProduct


admin.site.site_header = "Inventory Manager"
admin.site.site_title = "Inventory Manager Admin"
admin.site.index_title = "Welcome to the Inventory Management System"

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'art', 'description')
    search_fields = ('name', 'art')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity')
    search_fields = ('product__name', 'warehouse__name')

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('warehouse', 'date', 'supplier_name')
    search_fields = ('warehouse__name', 'supplier_name')

@admin.register(SuppliedProduct)
class SuppliedProductAdmin(admin.ModelAdmin):
    list_display = ('supply', 'product', 'quantity')
    search_fields = ('supply__id', 'product__name')
