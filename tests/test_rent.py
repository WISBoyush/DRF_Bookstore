import pytest

from rents.models import Rent


class TestRent:

    @pytest.mark.django_db
    def test_rent_list(self, api_client, user):
        url = '/api/rent/'

        response = api_client.get(url)
        assert response.status_code == 200
        assert Rent.objects.filter(
            user_id=user.pk, state="AWAITING_DELIVERY"
        ).values('orders_id').first()['orders_id'] == response.data[0]['orders_id']

    @pytest.mark.django_db
    def test_rent_list_detail(self, api_client, user):
        rent_order = Rent.objects.filter(
            user_id=user.pk, state="AWAITING_DELIVERY"
        ).first()
        url = f'/api/rent/list_detail/?orders_id={rent_order.orders_id}'

        response = api_client.get(url)
        assert response.status_code == 200
        assert Rent.objects.filter(
            user_id=user.pk, state="AWAITING_DELIVERY"
        ).values('orders_id').first()['orders_id'] == response.data['orders_id']

    
