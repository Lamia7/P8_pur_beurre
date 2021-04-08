from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .forms import MainSearchForm
from .models import Product, Category, Favorite
from users.models import User


def home(request):
    """Displays the home page"""
    main_search_form = MainSearchForm()  # instanciate form
    context = {
        "main_search_form": main_search_form,
        # key: variables we access from template
    }
    return render(request, "search/home.html", context)


def products(request):
    """Displays the result page with list of products according to user input"""
    if request.method == "POST":
        # get the value of name="" from template
        product_search = request.POST["product_search"]
        # products = query made to DB
        # query: max 6 pdcts where name contains value of product_search
        # normalized as in feed_db.py
        products = Product.objects.all().filter(
            name__contains=product_search.strip().lower().capitalize()
        )[:6]
        context = {
            # title in HTML will contain value of product_search
            "title": product_search,
            "products": products,
        }
        # send context to products.html template and render this template
        return render(request, "search/products.html", context)


def product(request, product_id):
    """Displays the product details page

    Args:
        product_id (int): Id of the product
    """
    # try:
    product = Product.objects.get(pk=product_id)
    context = {"product": product}
    # except Product.DoesNotExist:
    return render(request, "search/product.html", context)


def substitutes(request, product_id):
    """Displays the result page with list of substitutes for the selected product
    
    Args:
        product_id (int): Id of the product"""
    # Find product searched by user with id
    product_query = Product.objects.get(pk=product_id)

    # Find categories of the searched_product
    product_query_cat = Category.objects.filter(product__id=product_query.id)

    # Find max 9 substitutes with better nutriscore
    # and at least 3 categories in common
    substitutes = (
        Product.objects.filter(categories__in=product_query_cat)
        .annotate(nb_cat=Count("categories"))
        .filter(nb_cat__gte=3)
        .filter(nutriscore__lt=product_query.nutriscore)
        .order_by("nutriscore")[:9]
    )

    context = {"product": product_query, "substitutes": substitutes}

    return render(request, "search/substitutes.html", context)


@login_required
def save_favorite(request, product_id, substitute_id):
    """Saves the substitute and product searched as favorite
    if user is logged in"""

    product = Product.objects.get(pk=product_id)
    substitute = Product.objects.get(pk=substitute_id)
    user = User.objects.get(
        pk=request.user.id
    )  # request.user for current user connected
    favorite = Favorite(product=product, substitute=substitute, user=user)

    # Save this as a favorite in DB
    try:
        favorite.save()
        return redirect("search:favorites")
    except IntegrityError:
        return redirect("search:home")


@login_required
def favorites(request):
    """Displays the favorites for the logged in user"""

    # Find favorites in DB according to user id
    favorites = Favorite.objects.filter(user_id=request.user.id)

    context = {
        "favorites": favorites,
    }

    return render(request, "search/favorites.html", context)


def legal_notice(request):
    """Displays the legal notice page with infos"""
    return render(request, "search/legal_notice.html")
