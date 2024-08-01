from django.shortcuts import render
from store.models import Product,Cart,Order
from .forms import userInfoForm
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils.translation import gettext
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
import stripe
from django.template.loader import render_to_string
from .models import transaction,PaymentMethod
import math
from django.utils.translation import gettext
from django_store import settings
# Create your views here.




def strip_config(request):
    return JsonResponse({
        'public_key':settings.STRIPE_PUBLISHABLE_KEY
    })



def stripe_transaction(request):
    transaction=make_transaction(request,PaymentMethod.stripe)
    if not transaction:
        return JsonResponse({
    'message': gettext("Wrong information.")
}, status=400)
    stripe.api_key=settings.STRIPE_SECRET_KEY
    intent=stripe.PaymentIntent.create(
        amount=transaction.amount*100,
        currency=settings.CURRENCY,
        payment_method_types=['card'],
        metadata={
            'transaction':transaction.id,
        }
    )
    return JsonResponse({
        'client_secret':intent['client_secret']
    })

def paypal_transaction(request):
    transaction=make_transaction(request, PaymentMethod.Paypal)



def make_transaction(request,pm):
    form = userInfoForm(request.POST)
    if form.is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)
        total = 0
        for product in products:
            total += product.price

        if total <= 0:
            return None
        
        return transaction.objects.create(
            customer=form.cleaned_data,
            session=request.session.session_key,
            PaymentMethod=pm,
            items=cart.items,
            amount=math.ceil(total),
        )
    


