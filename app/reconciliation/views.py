from django.shortcuts import render, redirect
from .models import BankTransaction
import pandas as pd
from django.core.paginator import Paginator

def bank_transactions_view(request):
    transactions_list = BankTransaction.objects.all().order_by('-id')  # Order by id descending
    paginator = Paginator(transactions_list, 10)  # 10 per page

    page_number = request.GET.get('page')
    transactions = paginator.get_page(page_number)

    return render(request, 'reconciliation/bank_transactions.html', {'transactions': transactions})


def upload_transactions_view(request):
    message = ''
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        if uploaded_file.name.endswith('.csv') or uploaded_file.name.endswith('.xlsx'):
            try:
                # Read file directly from uploaded file (in-memory)
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

                # Check required columns
                required_columns = {'date', 'description', 'amount', 'reference_number'}
                if not all(col in df.columns for col in required_columns):
                    message = 'Missing required columns in file.'
                else:
                    for _, row in df.iterrows():
                        BankTransaction.objects.create(
                            date=row['date'],
                            description=row['description'],
                            amount=row['amount'],
                            reference_number=row['reference_number'],
                            company_id=1,
                            status='pending',
                            source_file_id=1 
                        )
                    message = 'File uploaded and data saved successfully.'

            except Exception as e:
                message = f'Error processing file: {str(e)}'
        else:
            message = 'Only CSV or XLSX files are allowed.'

    return render(request, 'reconciliation/upload.html', {'message': message})
