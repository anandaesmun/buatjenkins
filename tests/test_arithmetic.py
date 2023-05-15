from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import home, count, tambah


class test_arithmetic(SimpleTestCase):
    
    def test_tambah_func(self):
        result = tambah(7,5)
        assert result == 12