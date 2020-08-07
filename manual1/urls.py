from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('admin/', admin.site.urls),
]