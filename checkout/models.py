from django.db import models
from django.utils.translation import gettext
# Create your models here.



class TransActionStatus(models.IntegerChoices):
    Pending=0,gettext("Pending")
    Completed=1,gettext("Completed")

class PaymentMethod(models.IntegerChoices):
    stripe=1,gettext("Stripe")
    Paypal=2,gettext("Paypal")


class transaction(models.Model):
    session=models.CharField(max_length=255)
    amount=models.FloatField()
    items=models.JSONField()
    customer=models.JSONField()
    status=models.IntegerField(
        choices=TransActionStatus.choices,
        default=TransActionStatus.Pending,
    )
    PaymentMethod=models.IntegerField(
        choices=PaymentMethod.choices,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def customer_name(self):
        return self.customer['first_name']+' '+self.customer['last_name']
    
    @property
    def customer_email(self):
        return self.customer['email']

