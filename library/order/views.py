from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def orders(request):
    orders = Order.get_all()
    context = {
        'orders': orders,
        'title': "List of Orders"
    }
    return render(request, 'order/all_orders.html', context)

def order(request, order_id):
    order = Order.get_by_id(order_id=order_id)
    context = {
        'order': order,
    }
    return render(request, 'order/order_by_id.html', context)