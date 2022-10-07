from django.db import models

class Payment (models.Model):
    class PaymentMethod(models.Choices):
        cash = "1"
        credit_or_debit_card = "2"
        paypal = "3"

    payment_method = models.CharField(choices=PaymentMethod.choices , default=PaymentMethod.cash , max_length=25)
    total_amount = models.DecimalField(max_digits=3 , decimal_places=0)
    captured_amount = models.DecimalField(max_digits=3 , decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    