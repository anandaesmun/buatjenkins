from django.test import TestCase, Client
from django.urls import reverse


class test_views(TestCase):

    def test_home_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
