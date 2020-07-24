from django.test import TestCase
from django.urls import reverse
from .models import Note
from ..core import utils


class NoteTest(TestCase):

    @classmethod
    def setUp(self):
        self.user = utils.create_user()
        self.category = utils.create_category()

    def test_create(self):
        self.client.force_login(self.user)
        form_data = {'name':'foo', 'content':'dummy content', 'category':self.category.pk}
        response = self.client.post('/notes/'+str(self.category.pk)+'/create/', form_data)
        self.assertRedirects(response, reverse('categories:all'), status_code=302)
        self.assertEqual(len(Note.objects.all()), 1)


