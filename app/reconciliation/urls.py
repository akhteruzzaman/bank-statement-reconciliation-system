from django.urls import path
from .views import bank_transactions_view, upload_transactions_view

urlpatterns = [
    path('bank_transactions/', bank_transactions_view, name='bank_transactions'),
    path('upload/', upload_transactions_view, name='upload_transactions'),
]
