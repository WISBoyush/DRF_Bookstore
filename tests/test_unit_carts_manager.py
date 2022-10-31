import unittest

import pytest

from carts.models import Purchase
from main.models import Item
from users.models import User


class TestUnitCartManager(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User.objects.get(email='test@test.test')
        self.model = Purchase

    @pytest.mark.django_db
    def test_cart_list(self):
        cart = self.model.objects.filter(state="CART", user_id=self.user.pk).select_related('user_id').values_list(
            'id', 'item__price', 'item_id', 'user__profile__person_disc', 'amount'
        )

        item_ids = [
            [item[2], item[-1]]
            for item in cart
        ]

        items_discounted_price = [
            Item.objects.get(id=item[0]).price_discounted * item[1]
            for item in item_ids
        ]

        total = sum(items_discounted_price) - sum(items_discounted_price) * 0.01 * cart[0][3]
        self.assertEqual(
            total,
            self.model.objects.get_total_products_information(
                user_pk=self.user.pk,
                state=['CART']
            )['persons_discounted_price'])
