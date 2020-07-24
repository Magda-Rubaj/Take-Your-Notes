from django.test import TestCase
from django.urls import reverse
from .models import Category
from ..core import utils


class CategoryTest(TestCase):

    @classmethod
    def setUp(self):
        self.user = utils.create_user()

    def test_create(self):
        self.client.force_login(self.user)
        form_data = {'name':'foo', 'user':self.user.pk}
        response = self.client.post(reverse('categories:create'), form_data)
        self.assertRedirects(response, reverse('categories:all'), status_code=302)
        self.assertEqual(len(Category.objects.all()), 1)


