from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock','stock_sold', 'category', 'created_date', 'modified_date', 'is_available','is_like')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)