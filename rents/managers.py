from django.db import models, transaction
from django.db.models import Count


class RentManager(models.Manager):


    @transaction.atomic
    def add_entry_in_db(self, user_pk, item_id):
        self.create(
            state='CART',
            user_id=user_pk,
            item_id=item_id,
        )

    @transaction.atomic
    def delete_entry_in_db(self, item_id, user_pk):
        obj = self.filter(
            item_id=item_id,
            user_id=user_pk
        )

        obj.delete()

    def get_rents_order_information(self, orders_id):
        orders = self.filter(orders_id=orders_id)
        returned_data = {'orders_id': str(orders_id),
                         'orders': orders}

        return returned_data



