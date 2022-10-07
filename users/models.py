from datetime import datetime, timedelta

import jwt
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from DRF_bookstore import settings
from .managers import UserManager


class User(AbstractUser):
    objects = UserManager()
    username = None
    email = models.EmailField(
        _("email address"),
        max_length=150,
        unique=True,
        blank=False
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    first_name = None
    last_name = None

    def __str__(self):
        return self.email

    # @property
    # def token(self):
    #     return self._generate_jwt_token()
    #
    # def _generate_jwt_token(self):
    #     dt = datetime.now() + timedelta(days=1)
    #
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #
    #     return token.decode('utf-8')
