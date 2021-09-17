from django.urls import path
from .views import *

urlpatterns = [
    path('', orders),
    path('<int:order_id>/', order, name='order'),
]