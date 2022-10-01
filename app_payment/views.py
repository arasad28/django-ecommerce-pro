import imp
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
#model and form
from app_order.models import Order,Cart
from app_shop.models import Product
from .models import BillingAddress
from .forms import BillingForm

# ssl payment 
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
# stripe payment 
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.


class SuccessView(TemplateView):
    template_name = "app_payment/success.html"

class CancelView(TemplateView):
    template_name = "app_payment/cancel.html"
@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST,instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request,f"Shipping Address saved")
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()

    return render(request,"app_payment/checkout.html",context={'form':form,'order_items':order_items,'order_total':order_total,'saved_address':saved_address})


@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request,'Please Complete Shipping Address')
        return redirect('app_payment:checkout')
    if not request.user.profile.is_fully_filled():
        messages.info(request,f"Please complete Your Profile details")
        return redirect('app_login:profile')

    return render(request,'app_payment/payment.html')

@login_required
def pay_ssl(request):
    store_id = 'learn6255c58f3b3c9'
    API_KEY = 'learn6255c58f3b3c9@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_KEY)
    status_url = request.build_absolute_uri(reverse('app_payment:complete_ssl'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_items_count = order_qs[0].orderitems.count()
    order_total = order_qs[0].get_totals()


    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_items, num_of_item=order_items_count, shipping_method='Courier', product_profile='None')

    current_user = request.user
    mypayment.set_customer_info(name=current_user.profile.full_name, email=current_user.email, address1=current_user.profile.address, address2=current_user.profile.address, city=current_user.profile.city, postcode=current_user.profile.zip_code, country=current_user.profile.country, phone=current_user.profile.phone)
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    mypayment.set_shipping_info(shipping_to=current_user.profile.full_name, address=saved_address, city=saved_address.city, postcode=saved_address.zip_code, country=saved_address.country)

    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])

@csrf_exempt
def complete_ssl(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,"Your Payment Complete Successfully!page will be redirect after 5s")
            return HttpResponseRedirect(reverse("app_payment:purchase",kwargs={'val_id':val_id,'tran_id':tran_id},))
        elif status == 'FAILED':
            messages.warning(request,f"you payment failed! please try again later for complete payment successfully! page will be redirect after 5s")
    return render(request,'app_payment/complete_ssl.html')

class Complete_stripe(View):
    def post(self, request, *args, **kwargs):
        order_qs = Order.objects.filter(user=request.user,ordered=False)
        order_items = order_qs[0].orderitems.all()
        order_items_count = order_qs[0].orderitems.count()
        order_total = order_qs[0].get_totals()
        YOUR_DOMAIN = "http://127.0.0.1:8000/payment"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(order_total*100),
                        'product_data': {
                            'name': order_items,
                        },
                        },
                        
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)

def checkout_stripe(request):
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()

    return render(request,'app_payment/checkout_stripe.html',context={'order_total':order_total,'order_items':order_items,"STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY})

def paypal_pay(request):
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order_total = order_qs[0].get_totals()
    return render(request,'app_payment/paypal.html',context={'order_total':order_total})

@csrf_exempt
def payment_complete(request):
    body = json.loads(request.body)
    data = body["data"]
    val_id = data['orderID']
    tran_id = data['facilitatorAccessToken']
    # stat = body["status"]
    # print(id)
    # print(token)
    # print(stat)
    if val_id and tran_id:
        return HttpResponseRedirect(reverse("app_payment:purchase",kwargs={'val_id':val_id,'tran_id':tran_id},))

    return render(request,'app_payment/success.html')

@login_required
def purchase(request,val_id,tran_id):
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order = order_qs[0]
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.save()
    cart_items = Cart.objects.filter(purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()
    return HttpResponseRedirect(reverse('app_shop:home'))


