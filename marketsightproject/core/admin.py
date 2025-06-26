from django.contrib import admin
from .models import Product, Customer, Order, OrderItem, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    list_select_related = ('category',)  # Добавлено: загружает связанные данные
    ordering = ['category', 'name']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)  # Использован ProductAdmin
