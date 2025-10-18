from django.db import models
from account.models import Account

class JournalEntry(models.Model):
    date = models.DateField()
    description = models.TextField()
    debit_account = models.ForeignKey(
        Account,
        related_name='debit_entries',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Account Name"
    )
    credit_account = models.ForeignKey(
        Account,
        related_name='credit_entries',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Account Name"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.description[:30]}"

