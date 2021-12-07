from django.http import HttpResponse
import json
import decimal
from datetime import date, datetime
import environ
env = environ.Env(
    DEBUG=(bool, False)
)


def custom_response_formatter(response, status, is_log=False):
    if is_log:
        print('RESPONSE', str(response))

    return HttpResponse(
        json.dumps(response), status=status, content_type="application/json",
    )


