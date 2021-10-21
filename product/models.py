from django.urls import reverse
from category.models import Category
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Khi xóa category thì Product bị xóa
    images = models.ImageField(upload_to='photos/products')
    def __str__(self):
        return self.product_name