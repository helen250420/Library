from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('<int:book_id>/', book, name='book'),
    path('unorder/', no_order, name='unorder'),
]