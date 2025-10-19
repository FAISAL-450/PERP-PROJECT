from django.db import models
from account.models import Account

# 📌 Transaction Categories
TRANSACTION_TYPE_CHOICES = [
    ('RECEIPT', 'Receipt'),
    ('PAYMENT', 'Payment'),
    ('TRANSFER', 'Transfer'),
    ('ADJUSTMENT', 'Adjustment'),
]

# ✅ Status Dropdown
TRANSACTION_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('POSTED', 'Posted'),
    ('CANCELLED', 'Cancelled'),
]

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    reference = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    
    debit_account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Account Name",
        related_name="debit_transactions"  # ✅ Unique reverse accessor
    )
    credit_account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Account Name",
        related_name="credit_transactions"  # ✅ Unique reverse accessor
    )

    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reference} - {self.description}"
