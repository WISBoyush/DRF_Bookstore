import pytest
from rest_framework_simplejwt.tokens import RefreshToken

from carts.models import Purchase


class TestOrder:

    @pytest.mark.django_db
    def test_order_list(self, api_client, user):
        url = '/api/order/'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data[0]['total'] > 0

    @pytest.mark.django_db
    def test_order_detail_list(self, api_client, user):
        item_of_order = Purchase.objects.filter(
            user_id=user.pk,
            state__in=["AWAITING_PAYMENT", "PAID"]
        ).first()

        url = f'/api/order/detail/?orders_id={item_of_order.orders_id}'
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['orders_id'] == item_of_order.orders_id

    @pytest.mark.gjango_db
    def test_order_pay_that_already_paid(self, api_client, user):
        order_item = Purchase.objects.filter(user_id=user.pk, state='PAID').first()
        url = '/api/order/pay/'
        response = api_client.post(url, {'orders_id': order_item.orders_id})
        assert response.data['message'] == 'This order already has been paid'

    @pytest.mark.gjango_db
    def test_order_pay_without_balance(self, api_client, user):
        order_item = Purchase.objects.filter(user_id=user.pk, state='AWAITING_PAYMENT').first()
        url = '/api/order/pay/'
        response = api_client.post(url, {'orders_id': order_item.orders_id})
        assert response.data['message'] == 'You dont have enough money to pay for this order'

    @pytest.mark.gjango_db
    def test_order_pay_with_balance(self, api_client, user, superuser):
        order_item = Purchase.objects.filter(user_id=user.pk, state='AWAITING_PAYMENT').first()
        url = '/api/order/pay/'

        api_client.force_login(superuser)
        api_client.patch(f'/api/user/{user.pk}/profile/update_balance/', {'balance': 9999})

        api_client.logout()
        refresh = RefreshToken.for_user(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.post(url, {'orders_id': order_item.orders_id})
        assert response.data == 'Order was successfully paid'
