from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.log_in, name='login'),
    path('sign_up/', views.sign_up, name='sign up'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/', views.main, name='main'),
]