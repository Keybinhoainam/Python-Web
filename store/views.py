# from orders.models import OrderProduct
from django.contrib import messages
# from store.forms import ReviewForm
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Q

from orders.models import OrderProduct
from store.forms import ReviewForm
from store.models import Product, ReviewRating
from carts.models import Cart, CartItem
from category.models import Category
from carts.views import _cart_id


def store(request):

    products = Product.objects.all().filter(is_available=True).order_by('id')

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(products, 9)
    paged_products = paginator.get_page(page)
    product_count = products.count()
    categories = Category.objects.all().filter()

    context = {
        'products': paged_products,
        'product_count': product_count,
        'categories': categories,
    }
    return render(request, 'store/store.html', context=context)
def store2(request, category_slug):

    categories = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all().filter(category=categories, is_available=True)

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(products, 6)
    paged_products = paginator.get_page(page)
    product_count = products.count()
    categories = Category.objects.all().filter()
    context = {
        'products': paged_products,
        'product_count': product_count,
        'categories': categories,
        'category1':category_slug,
    }
    return render(request, 'store/store2.html', context=context)

def product_detail(request, category_slug, product_slug=None):
    categories = Category.objects.all().filter()
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        cart = Cart.objects.get(cart_id=_cart_id(request=request))
        in_cart = CartItem.objects.filter(
            cart=cart,
            product=single_product
        ).exists()
    except Exception as e:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    try:
        orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
    except Exception:
        orderproduct = None

    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
        'single_product': single_product,
        'in_cart': in_cart if 'in_cart' in locals() else False,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'category': category_slug,
        'categories': categories,
    }
    return render(request, 'store/product_detail.html', context=context)


def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        products = Product.objects.order_by('-created_date').filter(
            Q(product_name__icontains=q) | Q(description__icontains=q))
        product_count = products.count()
    context = {
        'products': products,
        'q': q,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context=context)

def searchPrice(request):
    if ('category' and 'min' and 'max') in request.GET:
        categories = Category.objects.all().filter()
        category = request.GET.get('category')
        min = request.GET.get('min')
        max = request.GET.get('max')
        if (str(category) == 'allProduct'):
            productPrice = Product.objects.order_by('-created_date').filter()
            products = []
            k = 0
            for product in productPrice:
                if (int(max) < 2000):
                    if (product.price >= int(min) and product.price <= int(max)):
                        products.append(product)
                        k += 1
                else:
                    if (product.price >= int(min)):
                        products.append(product)
                        k += 1
            product_count = k
        else:
            productPrice = Product.objects.order_by('-created_date').filter(
                Q(product_name__icontains=category))
            products = []
            k = 0
            for product in productPrice:
                if(int(max) < 2000):
                    if(product.price >= int(min) and product.price <= int(max)):
                        products.append(product)
                        k += 1
                else:
                    if (product.price >= int(min)):
                        products.append(product)
                        k += 1
            product_count = k

    context = {
        'products': products,
        'product_count': product_count,
        'category': category,
        'min': min,
        'max': max,
        'categories': categories,
    }
    return render(request, 'store/store.html', context=context)

def searchPrice2(request):
    if ('category' and 'min' and 'max') in request.GET:
        categories = Category.objects.all().filter()
        category = request.GET.get('category')
        min = request.GET.get('min')
        max = request.GET.get('max')
        if (str(category) == 'allProduct'):
            productPrice = Product.objects.order_by('-created_date').filter()
            products = []
            k = 0
            for product in productPrice:
                if (int(max) < 2000):
                    if (product.price >= int(min) and product.price <= int(max)):
                        products.append(product)
                        k += 1
                else:
                    if (product.price >= int(min)):
                        products.append(product)
                        k += 1
            product_count = k
        else:
            productPrice = Product.objects.order_by('-created_date').filter(
                Q(product_name__icontains=category))
            products = []
            k = 0
            for product in productPrice:
                if (int(max) < 2000):
                    if (product.price >= int(min) and product.price <= int(max)):
                        products.append(product)
                        k += 1
                else:
                    if (product.price >= int(min)):
                        products.append(product)
                        k += 1
            product_count = k

    context = {
        'products': products,
        'product_count': product_count,
        'category': category,
        'min': min,
        'max': max,
        'categories': categories,
    }
    return render(request, 'store/store2.html', context=context)

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Thank you! Your review has been updated.")
            return redirect(url)
        except Exception:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thank you! Your review has been submitted.")
                return redirect(url)

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Thank you! Your review has been updated.")
            return redirect(url)
        except Exception:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thank you! Your review has been submitted.")
                return redirect(url)
