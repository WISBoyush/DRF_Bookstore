import pytest

from rents.models import Rent


class TestCart:

    @pytest.mark.django_db
    def test_cart_update(self, api_client, user):
        url = '/api/cart/update_cart/'
        updates = {
            "cart": [
                {
                    'item_id': 1,
                    'amount': 5
                }
            ]
        }

        response = api_client.patch(url, updates, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_cart_list(self, api_client, user):
        url = '/api/cart/'
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_cart_make_order(self, api_client, user):
        url = '/api/cart/update_cart/'
        updates = {
            "cart": [
                {
                    'item_id': 1,
                    'amount': 5
                },
                {
                    'item_id': 2,
                    'amount': 3
                }
            ]
        }
        api_client.patch(url, updates, format='json')
        url = '/api/cart/make_order/'

        response = api_client.post(url, {'city': 'Moscow', 'address': 'Lenina, 7'}, follow=True)
        assert response.status_code == 200
        assert response.data['products'][0]['orders_id']
        assert api_client.get('/api/cart/').data['total'] == 0

    @pytest.mark.django_db
    def test_rent_cart_list(self, api_client, user):
        url = '/api/cart/rent/'
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_rent_cart_add_item(self, api_client, user):
        url = '/api/cart/rent/create_entry/'
        response = api_client.post(url, {"item_id": 6})
        assert response.status_code == 200
        assert Rent.objects.filter(user_id=user.pk, item_id=6).exists()

    @pytest.mark.django_db
    def test_rent_cart_make_order(self, api_client, user):
        url = '/api/cart/rent/create_entry/'
        api_client.post(url, {"item_id": 6})

        url = '/api/cart/rent/make_order/'
        response = api_client.post(
            url,
            {
                "city": "Moscow",
                "address": "Lenina, 7"
            }
        )
        assert response.status_code == 200
        assert Rent.objects.filter(user_id=user.pk, item_id=6, state='AWAITING_DELIVERY').exists()
