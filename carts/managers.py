from django.db import models

from main.models import Item
from profiles.models import Profile


class PurchaseManager(models.Manager):

    # Common.

    def get_personals_discounted_price(self):
        return self.total_products_inf['total'] - self.get_personal_discount() * self.total_products_inf['total']

    def get_total_price_of_buy(self):
        return sum([field['price_discounted'] for field in self.items_price])

    # FOR Cart.

    def get_personal_discount(self):
        return Profile.objects.filter(user_id=self.user_pk).first().person_disc * 0.01

    def total_price_discounted(self, state):
        products = list(self.filter(user_id=self.user_pk, state__in=state).order_by('id').values())

        for product in products:
            product_discounted_price = Item.objects.get(
                id=product['item_id']).price_discounted

            product['price_discounted'] = product['amount'] * product_discounted_price
            product['new_price'] = product_discounted_price

        return products

    def get_total_products_information(self, user_pk, state):
        self.user_pk = user_pk
        self.items_price = self.total_price_discounted(state)
        self.total_products_inf = dict()
        self.total_products_inf['total'] = self.get_total_price_of_buy()
        self.total_products_inf['persons_discounted_price'] = self.get_personals_discounted_price()
        self.total_products_inf['products'] = self.items_price

        return self.total_products_inf

    # FOR Order.

    def set_discounted_price_inf(self, orders_id):
        products = list(self.filter(user_id=self.user_pk, orders_id=orders_id).order_by('id').values())

        for product in products:
            product_discounted_price = Item.objects.get(
                id=product['item_id']).price_discounted

            product['price_discounted'] = product['amount'] * product_discounted_price
            product['new_price'] = product_discounted_price

        return products

    def get_total_orders_information(self, user_pk, orders_id):
        self.user_pk = user_pk
        self.items_price = self.set_discounted_price_inf(orders_id)
        self.total_products_inf = dict()
        self.total_products_inf['orders_id'] = orders_id
        self.total_products_inf['total'] = self.get_total_price_of_buy()
        self.total_products_inf['persons_discounted_price'] = self.get_personals_discounted_price()
        self.total_products_inf['products'] = self.items_price

        return self.total_products_inf
