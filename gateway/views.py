from django.shortcuts import render
from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from config import external_response_formatter
from config import sha256_convert
from _services.onepay_gateway import onepay_service


class RequestTransaction(views.APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            if ('amount' not in request.data or 'app_id' not in request.data or 'reference' not in request.data or
                    'customer_first_name' not in request.data or 'customer_last_name' not in request.data or
                    'customer_phone_number' not in request.data or 'customer_email' not in request.data or
                    'transaction_redirect_url' not in request.data):
                return external_response_formatter.custom_response_formatter({
                    "status": "00",
                    "message": "incomplete required fields"
                }, 200)

            data=request.data

            request_body={
                "amount": data["amount"],
                "app_id": data["app_id"],
                "reference": data["reference"],
                "customer_first_name": data["customer_first_name"],
                "customer_last_name": data["customer_last_name"],
                "customer_phone_number": data["customer_phone_number"],
                "customer_email": data["customer_email"],
                "transaction_redirect_url": data["transaction_redirect_url"]
            }

            hash_salt="hash salt"
            hash_body=sha256_convert.json_to_sha256_with_salt(request_body,hash_salt)

            response=onepay_service.request_transaction(request_body,hash_body)

            ipg_transaction_id = response["data"]["ipg_transaction_id"]
            gross_amount = response["data"]["amount"]["gross_amount"]
            discount = response["data"]["amount"]["discount"]
            handling_fee = response["data"]["amount"]["handling_fee"]
            net_amount = response["data"]["amount"]["net_amount"]
            currency = response["data"]["amount"]["currency"]
            redirect_url = response["data"]["gateway"]["redirect_url"]

            return external_response_formatter.custom_response_formatter({
                "status": "01",
                "message": "success",
            }, 200)

        except Exception as ex:
            return external_response_formatter.custom_response_formatter({
                "status": "00",
                "message": "Something went wrong"
            }, 200)


class WebHookView(views.APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:

            data = request.data

            onepay_transaction_id = data["onepay_transaction_id"]
            merchant_transaction_id = data["merchant_transaction_id"]
            hash_body = data["hash"]
            subscription_id = data["subscription_id"]
            status = data["status"]
            status_message = data["status_message"]
            paid_amount = data["paid_amount"]

            return external_response_formatter.custom_response_formatter({
                "status": "01",
                "message": "success",
            }, 200)

        except Exception as ex:
            return external_response_formatter.custom_response_formatter({
                "status": "00",
                "message": "Something went wrong"
            }, 200)