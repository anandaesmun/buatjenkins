from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import home, count
import pytest


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

        # tes url pake pytest
   # @pytest.mark.django.db
   # def test_home_url_pake_pytest(client):
    #    url = reverse('home')
     #   response = client.get(url)
      #  assert response.status_code == 200
    
