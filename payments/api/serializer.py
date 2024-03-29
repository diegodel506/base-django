from django.db import models
from rest_framework.serializers import ModelSerializer

from payments.models import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "table",
            "totalPayment",
            "statusPayment",
            "paymentType",
            "nit",
            "created_at",
            "name",
            "propina",
        ]
