from django.db.transaction import atomic

from profiles.models import Profile

from orders import errors


class OrderService:

    def list(self, user_pk, model, *args, **kwargs):
        users_orders = model.objects.filter(
            user_id=user_pk,
            state__in=['AWAITING_ARRIVAL',
                       'AWAITING_PAYMENT',
                       'PAID',
                       'AWAITING_DELIVERY',
                       'SENT',
                       'FINISHED'])
        data_to_serialize = []
        orders_ids = list((users_orders.values('orders_id').distinct('orders_id')))
        for orders_id in orders_ids:
            data_to_serialize.append(model.objects.get_total_orders_information(
                user_pk, orders_id['orders_id']
            ))

        return data_to_serialize

    def list_detail(self, orders_id, model, user_pk):
        return model.objects.get_total_orders_information(
            user_pk=user_pk, orders_id=orders_id
        )

    @atomic
    def pay(self, user_pk, orders_id, model):
        users_orders = model.objects.filter(
            orders_id=orders_id, state='AWAITING_PAYMENT')
        if not users_orders.exists():
            raise errors.AlreadyPaidError("This order already has been paid")

        users_profile = Profile.objects.get(id=user_pk)
        users_orders_detail = model.objects.get_total_orders_information(
            user_pk, orders_id
        )
        if users_profile.balance < users_orders_detail['persons_discounted_price']:
            raise errors.LackOfMoneyError("You dont have enough money to pay for this order")

        users_profile.balance -= users_orders_detail['persons_discounted_price']
        users_profile.save()
        users_orders.update(
            state='PAID'
        )
        return True
