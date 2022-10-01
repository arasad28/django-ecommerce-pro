from unicodedata import name
from django.urls import path
from app_payment import views
app_name = 'app_payment'
urlpatterns = [
    path('checkout/',views.checkout,name='checkout'),
    path('payment/',views.payment,name='payment'),
    path('pay_ssl/',views.pay_ssl,name='pay_ssl'),
    path('status/',views.complete_ssl,name='complete_ssl'),
    path('purchase/<val_id>/<tran_id>/',views.purchase,name='purchase'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('stripe-session/', views.Complete_stripe.as_view(), name='stripe_session'),
    path('checkout-stripe/',views.checkout_stripe,name='checkout_stripe'),
    path('paypal/',views.paypal_pay,name='paypal_pay'),
    path('paypal_sucess/',views.payment_complete,name='payment_complete'),
]