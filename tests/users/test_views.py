from django.test import TestCase, Client
from django.urls import reverse

from users.models import User


class TestUsersViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.account_url = reverse("account")
        self.user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="password1234",
        )
        # self.client.login(
        # email="user1@gmail.com",
        # password="password1234",
        # )
        self.client.force_login(self.user)

    def test_account_page(self):
        # check that reverse the account template
        # self.client.force_login(self.user)
        response = self.client.get(self.account_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account.html")
