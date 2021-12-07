from django.conf.urls import url
from rest_framework import routers
from .views import *

urlpatterns = [
    url(r"^request-transaction/$", RequestTransaction.as_view(), name="request-transaction"),
    url(r"^confirm/$", WebHookView.as_view(), name="confirm"),
]