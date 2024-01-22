from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "table",
        "totalPayment",
        "statusPayment",
        "paymentType",
        "created_at",
        "nit",
        "name",
        "propina",
    ]
