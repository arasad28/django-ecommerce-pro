from dataclasses import field
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.conf import settings

# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True)
    address = models.CharField(max_length=264,blank=True)
    zip_code = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return f'{self.user.profile.username} billing address'

    def is_fully_filled(self):
        field_name =[f.name for f in self._meta.get_fields()]
        for field_name in field_name:
            value = getattr(self,field_name)
            if value is None or value =='':
                return False
            return True
    class Meta:
        verbose_name_plural = 'Billing Address'