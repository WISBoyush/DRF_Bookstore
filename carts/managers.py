from django.db import models

from main.models import Item
from profiles.models import Profile


class PurchaseManager(models.Manager):

    # Common.

    # FOR Cart.

    def get_personal_discount(self, user_pk):
        return Profile.objects.filter(user_id=user_pk).first().person_disc * 0.01

    def total_price_discounted(self, user_pk, state):

        for product in self.filter(user_id=user_pk, state__in=state).order_by('id').values():
            product_discounted_price = Item.objects.get(
                id=product['item_id']
            ).price_discounted

            product['price_discounted'] = product['amount'] * product_discounted_price
            product['new_price'] = product_discounted_price
            yield product

    def get_total_products_information(self, user_pk, state):
        extra_products = list(self.total_price_discounted(user_pk, state))
        total = sum(
            field['price_discounted']
            for field in extra_products
        )
        return dict(
            total=total,
            persons_discounted_price=total - self.get_personal_discount(user_pk) * total,
            products=extra_products
        )

    # FOR Order.

    def set_discounted_price_inf(self, orders_id, user_pk):

        for product in self.filter(user_id=user_pk, orders_id=orders_id).order_by('id').values():
            product_discounted_price = Item.objects.get(
                id=product['item_id']).price_discounted

            product['price_discounted'] = product['amount'] * product_discounted_price
            product['new_price'] = product_discounted_price

            yield product

    def get_total_orders_information(self, user_pk, orders_id):
        extra_products = list(self.set_discounted_price_inf(orders_id, user_pk))
        total = sum(
            field['price_discounted']
            for field in extra_products
        )
        return dict(
            orders_id=orders_id,
            total=total,
            persons_discounted_price=total - self.get_personal_discount(user_pk) * total,
            products=extra_products
        )
