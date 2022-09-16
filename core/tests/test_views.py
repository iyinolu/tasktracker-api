from urllib import response
from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_user_list(self):
        response = self.client.get(self.user_list)
        self.assertEqual(response.status_code, 200)

    def test_user_can_register_correctly(self):
        response = self.client.post(self.user_creation, self.user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["email"], self.user_data.pop("email"))
        self.assertEqual(response.data["username"], self.user_data.pop("username"))
        self.assertEqual(response.data["first_name"], self.user_data.pop("first_name"))
        self.assertEqual(response.data["last_name"], self.user_data.pop("last_name"))
    
    def test_user_can_successfully_request_tokens(self):
        user = self.user_model.objects.create_user(**self.user_data)
        user.is_active = True
        user.save()
        response = self.client.post(self.token_request, self.login_info)
        self.assertEqual("access" in response.data.keys(), True)
        self.assertEqual("refresh" in response.data.keys(), True)