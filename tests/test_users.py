from pprint import pprint
from random import randint

import pytest
from django.urls import reverse


class TestUser:
    @pytest.mark.django_db
    def test_get_user_token(self, api_client, django_user_model):
        user = django_user_model.objects.create_user(email='test2@test.test', password='testtest2')
        url = reverse('token_obtain_pair')
        response = api_client.post(url, {
            'email': user.email, 'password': 'testtest2'
        })
        # assert 0
        assert response.status_code == 200
        assert response.data.get('access')

    @pytest.mark.django_db
    def test_users_profile(self, api_client, django_user_model, user):
        url = f'/api/user/{user.pk}/profile'
        response = api_client.get(url, follow=True)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_users_profile(self, api_client, django_user_model, user):
        url = f'/api/user/{user.pk}/profile/update_profile/'
        response = api_client.patch(url, {'bio': 'Всем привет'}, follow=True)
        assert response.status_code == 200
        assert response.data.get('bio') == 'Всем привет'

    @pytest.mark.django_db
    def test_update_not_users_profile(self, api_client, django_user_model, user):
        url = f'/api/user/{randint(1, 10000)}/profile/update_profile/'
        response = api_client.patch(url, {'bio': 'Всем привет'}, follow=True)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_update_users_profile_balance(self, api_client, django_user_model, user):
        url = f'/api/user/{user.pk}/profile/update_profile/'
        response = api_client.patch(url, {'balance': 1000}, follow=True)
        assert response.status_code == 403
