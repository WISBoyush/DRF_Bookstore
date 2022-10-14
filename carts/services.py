import uuid
from datetime import date, datetime, timedelta

from rest_framework.serializers import ValidationError

from carts.errors import UnexpectedItemError
from carts.models import Purchase
from carts.serializers import CartItemSerializer
from main.models import Item
from rents.models import Rent
from rents.serializers import RentItemSerializer


class CartsService:

    def __init__(self, user, model, *args, **kwargs):
        self.user = user
        self.model = model
        super().__init__(*args, **kwargs)

    def list(self):
        queryset = self.model.objects.filter(user_id=self.user, state='CART').order_by('id').values()
        returned_data = self.model.objects.get_total_products_information(self.user, ['CART'])

        for index, product in enumerate(returned_data['products']):
            product.update(queryset[index])

        return returned_data

    def make_order(self, data, model):
        items_to_update = Purchase.objects.filter(user_id=self.user, state='CART')

        total_orders_price = model.objects.get_total_products_information(self.user, ['CART'])
        items_objects = Item.objects.all()
        personal_orders_id = uuid.uuid4()
        orders_time = datetime.now()
        city = data.get('city')
        address = data.get('address')

        updated_fields = {
            'state': 'AWAITING_PAYMENT',
            'orders_id': personal_orders_id,
            'orders_time': orders_time,
            'city': city,
            'address': address,
            'total_orders_price': total_orders_price['persons_discounted_price']
        }

        if all([item.amount <= items_objects.get(id=item.item_id).quantity for item in items_to_update]):

            for item in items_to_update:
                instance = Item.objects.get(id=item.item_id)
                instance.quantity -= item.amount
                instance.save()

            items_to_update.update(**updated_fields)
        else:
            items_to_update.update(state='AWAITING_ARRIVAL')

        updated_datas = Purchase.objects.filter(**updated_fields).values()

        returned_data = Purchase.objects.get_total_orders_information(
            self.user, orders_id=updated_fields['orders_id']
        )

        for index, product in enumerate(returned_data['products']):
            product.update(updated_datas[index])

        return returned_data

    def update_cart(self, data, user, *args, **kwargs):
        serializer = CartItemSerializer(data=data["cart"], many=True)

        if not serializer.is_valid():
            raise ValidationError

        data = data["cart"]
        item_in_cart = Purchase.objects.filter(state="CART", user_id=user)
        returned_data = []

        for item in data:
            product = item_in_cart.filter(item_id=item['item_id'])

            if item["amount"] == 0 and product.exists():
                product.delete()
                continue

            if item["amount"] == 0 and not product.exists():
                continue

            found_item, is_created = Purchase.objects.get_or_create(
                state='CART',
                item_id=item['item_id'],
                user_id=self.user,
                warranty_days=14
            )

            found_item.amount = item["amount"]
            found_item.save()
            returned_data.append(found_item)

        return returned_data


class RentCartsService:
    def __init__(self, user, model, *args, **kwargs):
        self.user = user
        self.model = model
        super().__init__(*args, **kwargs)

    def create(self, data, *args, **kwargs):

        serializer = RentItemSerializer(data=data)

        if not serializer.is_valid():
            raise ValidationError

        data = serializer.data
        item_in_cart, is_created = Rent.objects.get_or_create(
            state='CART',
            item_id=data['item_id'],
            user_id=self.user
        )

        if not is_created:
            raise UnexpectedItemError("You have not rent more then one item of good")

        return item_in_cart

    def make_order(self, data):
        items_to_update = Rent.objects.filter(user_id=self.user, state='CART')
        items_objects = Item.objects.all()
        personal_orders_id = uuid.uuid4()
        city = data.get('city', '12345')
        address = data.get('address', '12345')
        updated_fields = {
            'state': 'AWAITING_DELIVERY',
            'orders_id': personal_orders_id,
            'city': city,
            'address': address,
            'rented_from': date.today(),
            'rented_to': date.today() + timedelta(days=14),
        }

        if all([1 <= items_objects.get(id=item.item_id).quantity for item in items_to_update]):
            for item in items_to_update:
                instance = Item.objects.get(id=item.item_id)
                instance.quantity -= 1
                instance.save()

            items_to_update.update(**updated_fields)
        else:
            items_to_update.update(state='AWAITING_ARRIVAL')

        returned_data = Rent.objects.get_rents_order_information(
            orders_id=updated_fields['orders_id']
        )

        return returned_data
