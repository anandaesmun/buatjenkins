from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import home, count


class test_urls(SimpleTestCase):
    
    #tes url
    def test_home_urls_resolves(self):
        #assert 1 == 1
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_count_urls_resolves(self):
        #assert 1 == 1
        url = reverse('count')
        self.assertEqual(resolve(url).func, count)
        