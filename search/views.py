from django.shortcuts import render

from .forms import MainSearchForm
from .models import Product


def home(request):
    main_search_form = MainSearchForm()  # instanciate form
    context = {
        "main_search_form": main_search_form,  # key: variables we access from template
    }
    return render(request, 'search/home.html', context)


def products(request):
    if request.method == "POST":
        # get the value of name="" from template
        product_search = request.POST['product_search']
        # products = query made to DB
        # query: max 6 pdcts where name contains value of product_search normalized as in feed_db.py
        products = Product.objects.all().filter(
            name__contains=product_search.strip().lower().capitalize())[:6]
        context = {
            # title in HTML will contain value of product_search
            'title': product_search,
            'products': products,
        }
        # send context to products.html template and render this template
        return render(request, "search/products.html", context)


def product(request, product_id):
    #try:
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    #except Product.DoesNotExist:
    return render(request, 'search/product.html', context)
