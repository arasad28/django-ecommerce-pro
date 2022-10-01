from django.contrib import admin
from .models import Cart,Order,Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Comment)