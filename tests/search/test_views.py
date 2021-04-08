from django.test import TestCase, Client
from django.urls import reverse

from search.forms import MainSearchForm
from search.views import home


class TestHomeView(TestCase):

    def setUp(self):
       self.client = Client()

    def test_homepage(self):
        # check that reverse the home template
        response = self.client.get(reverse("search:home"))

        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, "search/home.html")
        # check if home template contains this on HTML 
        #self.assertContains(response, "product_search")


class TestProductsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_products_page_POST(self):
        product_search = {"product_search": "input"}

        #results = product_search
        response = self.client.post(reverse("search:products"), data=product_search)

        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, "search/products.html")


