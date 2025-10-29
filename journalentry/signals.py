from django.db.models.signals import post_save
from django.dispatch import receiver
from transaction.models import Transaction
from journalentry.models import JournalEntry
@receiver(post_save, sender=Transaction)
def generate_journal_entries(sender, instance, created, **kwargs):
    if instance.status != 'POSTED':
        return
    instance.journal_entries.all().delete()
    entries = []
    if instance.debit_account:
        entries.append(JournalEntry(
            transaction=instance,
            account=instance.debit_account,
            entry_type='DEBIT',
            amount=instance.amount,
            date=instance.date
        ))

    if instance.credit_account:
        entries.append(JournalEntry(
            transaction=instance,
            account=instance.credit_account,
            entry_type='CREDIT',
            amount=instance.amount,
            date=instance.date
        ))
    JournalEntry.objects.bulk_create(entries)
