from django.db import models
from account.models import Account
from transaction.models import Transaction
ENTRY_TYPE_CHOICES = [
    ('DEBIT', 'Debit'),
    ('CREDIT', 'Credit'),
]
class JournalEntry(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='journal_entries')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=6, choices=ENTRY_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.entry_type} | {self.account.name} | {self.amount}"


