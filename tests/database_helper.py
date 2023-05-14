import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_user():
    User.objects.create_user('agri2', 'afryanto@email.com', '123456')
    assert User.objects.count() == 1