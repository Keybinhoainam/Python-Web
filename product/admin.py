from django.contrib import admin

# Register your models here.
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)