from django.urls import path
from .views import bank_transactions_view

urlpatterns = [
    path('bank_transactions/', bank_transactions_view, name='bank_transactions'),
]
