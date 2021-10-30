from django.shortcuts import render
from store.models import Product, Category

def home(request):
    products = Product.objects.all().filter(is_available=True)
    products=sorted(products, key=lambda x:x.stock_sold,reverse=True )
    categories = Category.objects.all().filter()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home.html', context=context)
