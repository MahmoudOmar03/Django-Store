from django.contrib import admin
from django.urls import path
from . import views
from store import views as e
from checkout import webhooks
urlpatterns = [
    path('stripe/config',views.strip_config,name='checkout_stripe_config'), # type: ignore
    path('stripe/webhook',webhooks.stripe_webhook), # type: ignore
    path('stripe',views.stripe_transaction,name='checkout_stripe_transaction'), # type: ignore
    path("paypal",views.paypal_transaction,name="checkout_paypal"), # type: ignore
    path('checkout',e.checkout_complete , name='store.checkout_complete'),
]
