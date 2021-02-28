from django.contrib import admin

from search.models import Product, Category

# Registered models to access via 'admin' page
admin.site.register(Product)
admin.site.register(Category)