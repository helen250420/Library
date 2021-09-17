from django.urls import path
from .views import *

urlpatterns = [
    path('', users),
    path('<int:user_id>/', user, name='user')
]