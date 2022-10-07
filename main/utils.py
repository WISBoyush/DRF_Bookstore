import json

from django.http.response import HttpResponse


def get_4xx_or_error_message_json(status, message):
    return HttpResponse(json.dumps(
        {'error': message, }
    ), status=status,
        content_type='application/json', )
