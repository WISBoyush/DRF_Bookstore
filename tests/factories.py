import datetime
import random

import factory
from django.contrib.contenttypes.models import ContentType

from carts.models import Purchase
from main.models import (
    Item,
    Book,
    Figure
)
from rents.models import Rent
from tags.models import Tag
from users.models import User


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    tag_title = factory.Sequence(lambda n: "Tag %d" % n)
    tag_description = factory.Faker('text')
    discount = random.randint(5, 30)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    title = factory.Sequence(lambda n: "Item %d" % n)
    description = factory.Faker('text')
    price = random.randint(100, 400)
    image = factory.Faker('sentence', nb_words=2)
    quantity = random.randint(200, 300)
    content_type = factory.Iterator(ContentType.objects.all())

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)


class BookFactory(ProductFactory):
    class Meta:
        model = Book

    author = factory.Sequence(lambda n: "Author %d" % n)
    date_of_release = factory.Faker('date')


class FigureFactory(ProductFactory):
    class Meta:
        model = Figure

    manufacturer = factory.Sequence(lambda n: "Manufacturer %d" % n)


state_list = ['PAID', 'AWAITING_PAYMENT', 'AWAITING_DELIVERY']


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    user = factory.Iterator(User.objects.all())
    item = factory.Iterator(Item.objects.all())
    amount = random.randint(2, 5)
    city = factory.Sequence(lambda n: "City %d" % n)
    address = factory.Sequence(lambda n: "Address %d" % n)
    warranty_days = 14


class RentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rent

    user = factory.Iterator(User.objects.all())
    item = factory.Iterator(Item.objects.all())
    city = factory.Sequence(lambda n: "City %d" % n)
    address = factory.Sequence(lambda n: "Address %d" % n)
    rented_from = datetime.datetime.now()
    rented_to = datetime.datetime.now() + datetime.timedelta(days=14)


