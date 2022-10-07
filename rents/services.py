class RentService:

    def list(self, user_pk, model, *args, **kwargs):
        users_orders = model.objects.filter(
            user_id=user_pk,
            state__in=['AWAITING_ARRIVAL',
                       'AWAITING_DELIVERY',
                       'SENT',
                       'FINISHED'])
        data_to_serialize = []
        orders_ids = list((users_orders.values('orders_id').distinct('orders_id')))
        for orders_id in orders_ids:
            data_to_serialize.append(model.objects.get_rents_order_information(orders_id=orders_id['orders_id']))
        return data_to_serialize

    def list_detail(self, orders_id, model, user_pk):
        return model.objects.get_rents_order_information(orders_id=orders_id)

