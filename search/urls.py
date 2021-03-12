from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("products/", views.products, name="products"),
]

"""
from search import views as search_views

urlpatterns = [
    path('', search_views.home, name="home"),
    path('home/', search_views.home, name="home"),
    path('products/', search_views.products, name="products")
]
"""
