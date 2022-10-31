import datetime

import pytest


class TestMain:
    @pytest.mark.django_db
    def test_item_list(self, api_client, user):
        url = '/api/bookstore/items/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data != []

    @pytest.mark.django_db
    def test_book_list(self, api_client, user):
        url = '/api/bookstore/book/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data != []

    @pytest.mark.django_db
    def test_figure_list(self, api_client, user):
        url = '/api/bookstore/figure/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data != []

    @pytest.mark.django_db
    def test_book_detail(self, api_client, user, ):
        url = '/api/bookstore/book/1/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data.get('title') == 'Item 0'

    @pytest.mark.django_db
    def test_figure_detail(self, api_client, user):
        url = '/api/bookstore/figure/2/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data.get('title') == 'Item 1'

    @pytest.mark.django_db
    def test_u_book_create(self, api_client, user):
        url = '/api/bookstore/book/'
        item = {
            'title': 'Алхимия',
            'description': 'Синяя',
            'price': 250,
            'quantity': 100,
            'content_type_id': 8,
            'author': 'Менделеев',
            'date_of_release': datetime.date.today()
        }
        response = api_client.post(url, item)
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_su_book_create(self, api_client, superuser):
        url = '/api/bookstore/book/'
        item = {
            'title': 'Алхимия',
            'description': 'Синяя',
            'price': 250,
            'quantity': 100,
            'content_type_id': 8,
            'author': 'Менделеев',
            'date_of_release': '2022-08-09',
            'tags': [
                1, 2
            ],
        }
        response = api_client.post(url, item, format='json')
        assert response.status_code == 201
        assert response.data.get('title') == 'Алхимия'

    @pytest.mark.django_db
    def test_u_book_update(self, api_client, user):
        url = '/api/bookstore/book/1/update_item/'
        item = {
            'title': 'Неалхимия',
            'description': 'Красная',
            'tags': [
                1, 2, 4
            ],
        }
        response = api_client.patch(url, item, format='json')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_su_book_update(self, api_client, superuser):
        url = '/api/bookstore/book/1/update_item/'
        item = {
            'title': 'Неалхимия',
            'description': 'Красная',
            'tags': [
                1, 2, 4
            ],
        }
        response = api_client.patch(url, item, format='json')
        assert response.status_code == 200
        assert response.data.get('title') == 'Неалхимия'
