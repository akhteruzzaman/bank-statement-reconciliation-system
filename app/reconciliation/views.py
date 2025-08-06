from django.shortcuts import render, redirect
from .models import BankTransaction
import pandas as pd
from django.core.files.storage import FileSystemStorage

def bank_transactions_view(request):
    transactions = BankTransaction.objects.all()
    return render(request, 'reconciliation/bank_transactions.html', {'transactions': transactions})

def upload_transactions_view(request):
    message = ''
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        if uploaded_file.name.endswith('.csv') or uploaded_file.name.endswith('.xlsx'):
            try:
                # Save uploaded file temporarily
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)
                file_path = fs.path(filename)

                # Read file
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)

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

                fs.delete(filename)

            except Exception as e:
                message = f'Error processing file: {str(e)}'
        else:
            message = 'Only CSV or XLSX files are allowed.'

    return render(request, 'reconciliation/upload.html', {'message': message})
