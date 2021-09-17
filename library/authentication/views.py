from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from order.models import *

def users(request):
    users = CustomUser.get_all()
    context = {
        'users': users,
        'title': 'List of Users'
    }
    return render(request, 'authentication/all_users.html', context)

def user(request, user_id):
    user = CustomUser.get_by_id(user_id=user_id)
    orders = Order.objects.filter(user__id=user_id)
    context = {
        'user': user,
        'orders': orders,
        'title': f'{user.first_name} {user.last_name}'
    }
    return render(request, 'authentication/user_by_id.html', context)
