from django.test import TestCase
from django.urls import reverse
from ..core import utils

class UserAccessTest(TestCase):

    @classmethod
    def setUp(self):
        self.user = utils.create_user()
        self.dummy_category = utils.create_category()
        self.dummy_note = utils.create_note()

    def test_non_logged_access(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('categories:all'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('categories:create'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('categories:detail', kwargs={'pk': str(self.dummy_category.pk)}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/notes/'+str(self.dummy_category.pk)+'/create/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('notes:detail', kwargs={'pk': str(self.dummy_note.pk)}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('notes:edit', kwargs={'pk': str(self.dummy_note.pk)}))
        self.assertEqual(response.status_code, 302)


    
    def test_logged_access(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('categories:all'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('categories:create'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('categories:detail', kwargs={'pk': str(self.dummy_category.pk)}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/notes/'+str(self.dummy_category.pk)+'/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('notes:detail', kwargs={'pk': str(self.dummy_note.pk)}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('notes:edit', kwargs={'pk': str(self.dummy_note.pk)}))
        self.assertEqual(response.status_code, 200)

