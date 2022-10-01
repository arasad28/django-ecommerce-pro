from dataclasses import fields
from django import forms
from app_payment.models import BillingAddress

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields=['address','zip_code','city','country']