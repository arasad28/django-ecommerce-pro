from dataclasses import fields
from django import forms
# from stripe import Product
from .models import Product
from app_order.models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('author','created','q_deal',)
        widgets = {
            'full_description': SummernoteWidget(),
        }