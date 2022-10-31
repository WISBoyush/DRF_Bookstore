import random
import uuid

import pytest
from django.contrib.contenttypes.models import ContentType
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import (
    BookFactory,
    FigureFactory,
    TagFactory,
    OrderFactory,
    RentFactory
)
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db, django_user_model, api_client):
    user = django_user_model.objects.get(email='test@test.test')
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return user


@pytest.fixture
def superuser(db, django_user_model, api_client):
    user = django_user_model.objects.get(email='admin@admin.admin')
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return user


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():

        # Create User/Superuser.

        user = User.objects.create_user(email='test@test.test', password='testtest')
        User.objects.create_superuser(email='admin@admin.admin', password='admin')

        tags = [TagFactory.create(discount=random.randint(5, 20)) for _ in range(5)]
        for _ in range(5):
            BookFactory.create(
                content_type=ContentType.objects.get(model='book'),
                tags=[tags[random.randint(0, 4)], tags[random.randint(0, 4)]]
            )
            FigureFactory.create(
                content_type=ContentType.objects.get(model='figure'),
                tags=[tags[random.randint(0, 4)], tags[random.randint(0, 4)]]
            )
        state_list = ['CART', 'AWAITING_PAYMENT', 'PAID']
        rent_state_list = ['CART', 'AWAITING_DELIVERY']

        # Create items with other models.

        for i in range(3):
            orders_id = str(uuid.uuid4())
            state = state_list[i]
            for _ in range(2):
                data = dict(
                    user=user, state=state, city='12345', address='12345'
                ) if state == "CART" else dict(
                    user=user, orders_id=orders_id, state=state
                )

                OrderFactory.create(**data)

        for i in range(2):
            orders_id = str(uuid.uuid4())
            state = rent_state_list[i]
            for _ in range(2):
                if state == "CART":
                    RentFactory.create(user=user, state=state, city='12345', address='12345')
                    continue
                RentFactory.create(user=user, orders_id=orders_id, state=state)
