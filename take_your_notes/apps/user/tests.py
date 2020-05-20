from django.test import TestCase
from django.urls import reverse_lazy
from .models import User

class UserAccessTest(TestCase):

    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='someemail@mail.com',
            password='testpassword'
        )

    def test_non_logged_access(self):
        response = self.client.get(reverse_lazy('core:home'))
        self.assertEqual(response.status_code, 302)
    
    def test_logged_access(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('core:home'))
        self.assertEqual(response.status_code, 200)

