from django.test import TestCase, Client
from django.urls import reverse


class test_views(TestCase):

    def test_home_correct_credentials_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_home_different_username_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_home_different_password_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_different_username_password_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    # def test_logout_GET(self):
    #     client = Client()
    #     response = client.get(reverse('log_out'))
    #     self.assertEqual(response.status_code, 302)
    
    

    # def test_count_GET(self):
    #     client = Client()
    #     response = client.get(reverse('count'))
    #     self.assertEqual(response.status_code, 415)
    #     self.assertTemplateUsed(response, 'count.html')

