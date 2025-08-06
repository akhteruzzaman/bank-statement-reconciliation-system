import uuid
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class FileUploadStatus(models.Model):
    file_name = models.CharField(max_length=255)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)

class BankTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.TextField()  # Changed to TextField
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference_number = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100, null=True, blank=True)  # New field
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.date} | {self.description} | {self.amount}"
