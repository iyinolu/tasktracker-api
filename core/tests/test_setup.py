from rest_framework.test import APITestCase
from django.urls import reverse
from core.models import User


class TestSetup(APITestCase):
    def setUp(self):
        self.user_model = User
        self.user_list = reverse("user-crud-list")
        self.user_creation = reverse("signin-list")
        self.token_request = reverse("token_obtain_pair")
        self.user_data = {
            "first_name": "unit",
            "last_name": "tests",
            "username": "unittests",
            "email": "unittest@mail.com",
            "password": "testing321"
        }
        self.login_info = {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
