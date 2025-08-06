import uuid
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class FileUploadStatus(models.Model):
    file_name = models.CharField(max_length=255)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)

class BankTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)  # Using BigInt for simplicity; use UUIDField if preferred
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference_number = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    source_file = models.ForeignKey(FileUploadStatus, on_delete=models.CASCADE)
    matched_invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.date} | {self.description} | {self.amount}"
