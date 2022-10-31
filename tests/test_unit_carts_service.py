import unittest

import pytest

from carts.errors import UnexpectedItemError
from carts.models import Purchase
from carts.services import CartsService, RentCartsService
from rents.models import Rent
from users.models import User


class TestUnitCart(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User.objects.get(email='test@test.test')
        self.model = Purchase
        self.service = CartsService(self.user, self.model)

    @pytest.mark.django_db
    def test_cart_list(self):
        cart = self.model.objects.filter(user_id=self.user.pk, state="CART").order_by('id')
        self.assertEqual(
            [tuple(item.values())[0:-2] for item in self.service.list()['products']],
            list(cart.values_list())
        )

    @pytest.mark.django_db
    def test_cart_make_order(self):
        items_in_cart = self.model.objects.filter(
            user_id=self.user.pk,
            state="CART"
        ).values_list('id')[:][1]

        payload = {
            "address": "Lenina, 7",
            "city": "Moscow"
        }

        self.service.make_order(data=payload, model=self.model)
        self.assertEqual(self.model.objects.filter(id__in=items_in_cart).first().state, "AWAITING_PAYMENT")

        with self.assertRaises(UnexpectedItemError):
            self.service.make_order(data=payload, model=self.model)

    @pytest.mark.django_db
    def test_update_cart(self):
        payload = {
            "cart": [
                {
                    "item_id": 2,
                    "amount": 5
                },
                {
                    "item_id": 8,
                    "amount": 10
                },
                {
                    "item_id": 1,
                    "amount": 0
                }
            ]
        }

        self.service.update_cart(data=payload, user=self.user)
        updated_items = Purchase.objects.filter(
            item_id__in=list(item["item_id"] for item in payload["cart"][0:-1]),
            user_id=self.user.pk,
            state="CART"
        )

        self.assertEqual(
            list(
                updated_items.values('amount', 'item_id').order_by('item_id')
            ),
            payload["cart"][0:-1]
        )

        self.assertFalse(updated_items.filter(item_id=1).exists())

        # Alternative version

        # for item in payload["cart"]:
        #     if item["amount"] == 0:
        #         self.assertFalse(
        #             Purchase.objects.filter(
        #                 user_id=self.user.pk,
        #                 state="CART",
        #                 item_id=item["item_id"]
        #             ).exists()
        #         )
        #         continue
        #
        #     self.assertEqual(
        #         Purchase.objects.get(
        #             user_id=self.user.pk,
        #             state="CART",
        #             item_id=item["item_id"]).amount,
        #         item["amount"]
        #     )


class TestUnitRentCart(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User.objects.get(email='test@test.test')
        self.model = Rent
        self.service = RentCartsService(self.user, self.model)

    @pytest.mark.django_db
    def test_rent_cart_create(self):
        payload = {
            "item_id": 4
        }
        self.service.create(payload)
        self.assertTrue(self.model.objects.filter(state="CART", item_id=4, user_id=self.user.pk).exists())

        with self.assertRaises(UnexpectedItemError):
            self.service.create(payload)

    @pytest.mark.django_db
    def test_rent_cart_make_order(self):
        payload = {
            "address": "Lenina, 7",
            "city": "Moscow"
        }

        order = self.service.make_order(payload)['orders'][0]

        self.assertEqual(order.city, payload['city'])
        self.assertEqual(order.address, payload['address'])
        self.assertEqual(order.state, 'AWAITING_DELIVERY')
