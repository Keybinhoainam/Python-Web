from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store2, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('searchPrice/', views.searchPrice, name='searchPrice'),
    path('searchPrice2/', views.searchPrice2, name='searchPrice2'),
    path('submit_review/<int:product_id>/',views.submit_review, name='submit_review'),
    path('like/<int:product_id>/',views.like, name='like'),

]
