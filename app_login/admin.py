from pyexpat import model
from statistics import mode
from django.contrib import admin
from app_login.models import User,Profile
from app_order.models import Comment
from app_order.models import Order
# Register your models here.

class Modeladmin(admin.ModelAdmin):
    list_display = [
        'user',
        'username',
        'full_name',
        'address',
        'city',
        'zip_code',
        'country',
        'phone',
        'date_joined',
        'seller',
    ]
    list_display_links = [
        'user',
        'username',
        'full_name',
        'address',
        'city',
        'zip_code',
        'country',
        'phone',
    ]
    list_filter = [
        'country',
        'seller',
    ]
    search_fields = ['user__email']
admin.site.register(User)
admin.site.register(Profile,Modeladmin)
