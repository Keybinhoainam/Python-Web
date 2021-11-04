from django.urls import path
from . import views
from greatkart import views as vieww

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/',views.edit, name='edit'),
    # path('', views.dashboard, name='dashboard'),
    path('', vieww.home, name='home'),
]