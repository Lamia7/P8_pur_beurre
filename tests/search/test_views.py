from django.test import TestCase, Client
from django.urls import reverse

# from search.forms import MainSearchForm
from search.models import Product


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse("search:home")
        self.products_list_url = reverse("search:products")
        Product.objects.create(id=713, name="Nutella biscuits", nutriscore="E")
        self.product_details_url = reverse("search:product", args=[713])

    def test_homepage(self):
        # check that reverse the home template
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/home.html")
        # check if home template contains this on HTML
        self.assertContains(response, "product_search")

    def test_products_page_POST(self):
        product_search = {"product_search": "input"}

        # results = product_search
        response = self.client.post(
            self.products_list_url, data=product_search
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/products.html")

    def test_product_details_page(self):
        response = self.client.get(self.product_details_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].name, "Nutella biscuits")
        self.assertTemplateUsed(response, "search/product.html")
