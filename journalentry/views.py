from django.shortcuts import render
from .models import JournalEntry
def journal_dashboard(request):
    entries = JournalEntry.objects.select_related('transaction', 'account').order_by('-date')
    return render(request, "journalentry/journalentry_dashboard.html", {"entries": entries})

