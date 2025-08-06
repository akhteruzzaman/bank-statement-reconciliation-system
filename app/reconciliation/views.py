from django.shortcuts import render
from .models import BankTransaction

def bank_transactions_view(request):
    transactions = BankTransaction.objects.all()
    return render(request, 'reconciliation/bank_transactions.html', {'transactions': transactions})
