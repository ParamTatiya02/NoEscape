from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home1'),
    path('contact/', views.contact, name='contact'),
    path('complaint/', views.complaint, name='complaint'),
    path('about/', views.about, name='about'),
    path('evidence/', views.evidence, name='evidence'),
    path('profile/', views.main, name='main'),
]