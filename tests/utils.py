from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def do_as_superuser(superuser, user):
    def _do_as_superuser(func):
        def operaion(*args, **kwargs):
            client = APIClient()
            refresh = RefreshToken.for_user(superuser)
            client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
            func(client, *args, **kwargs)
            client.logout()
            refresh = RefreshToken.for_user(user)
            client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        return operaion

    return _do_as_superuser
