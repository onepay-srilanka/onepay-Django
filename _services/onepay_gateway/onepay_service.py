import requests
import json
import datetime
import base64

transaction_request_url="https://merchant-api-live-v2.onepay.lk/api/ipg/gateway/request-transaction/"
app_token="test_key"


def request_transaction(request_body,hash_body):
    api_url = transaction_request_url+"?"+"hash="+hash_body

    headers = {
        'Content-Type': 'application/json',
        'Authorization': "438092d19904343b0baa6d77376a22df6ff2b104ec9a524098b7406f5e50e3e07a9fceeadd0ff522.FXMS1187AEA68DE9D6DF1"
    }

    try:
        response = requests.get(url=api_url, headers=headers, data=json.dumps(request_body))

        try:
            response_obj = response.json()
        except ValueError:
            response_obj=response.content

        print(response_obj)

        return {
            'status': True,
            'status_code': response.status_code,
            'response': response_obj
        }

    except requests.exceptions.RequestException:
        return {
            'status': False,
            'status_code': "00",
            'response': {}
        }

    except Exception as ex:
        return {
            'status': False,
            'status_code': "00",
            'response': {}
        }











