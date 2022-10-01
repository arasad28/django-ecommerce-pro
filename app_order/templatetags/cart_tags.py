from atexit import register
from django import template
from app_order.models import Order

register = template.Library()

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user,ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0

@register.filter
def total(user):
    order_qs = Order.objects.filter(user=user,ordered=False)
    order_total = order_qs[0].get_totals()
    if order_total:
        return order_total
    return 0