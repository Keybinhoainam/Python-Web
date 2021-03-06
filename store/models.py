from django.urls import reverse
from accounts.models import Account
from category.models import Category
from django.db import models
from accounts.models import Account

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=10000, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(default=100)
    stock_sold = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Khi xóa category thì Product bị xóa
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_like=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
