from django.contrib import admin
from .models import Category,Product,Slider
from app_order.models import Comment
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin



def q_deal_accepted(modeladmin, request, queryset):
    queryset.update(q_deal_req=False, q_deal=True)


q_deal_accepted.short_description = 'Quick Deal Accept'
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('user','comment',)
class PostAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    summernote_fields = ('full_description',)
    list_display = [
        'title',
        'q_deal',
        'q_deal_req',
        'category',
    ]
    list_filter = ['q_deal','q_deal_req','category',]
    inlines =[CommentInline]
    actions = [q_deal_accepted,]
    


admin.site.register(Category)
admin.site.register(Product,PostAdmin)
admin.site.register(Slider)

