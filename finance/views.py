from django.shortcuts import render
from account.models import Account
from journalentry.models import JournalEntry
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# 🔁 Reusable Pagination Function
def get_paginated_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")
    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

# 💼 Finance Account Detailed View
def finance_ac_list(request):
    query = request.GET.get('q', '').strip()
    accounts = Account.objects.all()
    if query:
        accounts = accounts.filter(name__icontains=query)

    accounts_page = get_paginated_queryset(request, accounts, per_page=10)

    return render(request, 'finance/finance_ac_list.html', {
        'accounts': accounts_page,
        'query': query
    })

# 📘 Finance Transaction Entry Detailed View
def finance_tn_list(request):
    query = request.GET.get('q', '').strip()
    transactions = Transaction.objects.all()
    if query:
        transactions = transactions.filter(status__icontains=query)
    transactions_page = get_paginated_queryset(request, transactions, per_page=10)
    return render(request, 'finance/finance_tn_list.html', {
        'transactions': transactions_page,
        'query': query
    })

# 📘 Finance Journal Entry Detailed View
def finance_je_list(request):
    query = request.GET.get('q', '').strip()
    journalentries = JournalEntry.objects.all()
    if query:
        journalentries = journalentries.filter(description__icontains=query)

    journalentries_page = get_paginated_queryset(request, journalentries, per_page=10)

    return render(request, 'finance/finance_je_list.html', {
        'journalentries': journalentries_page,
        'query': query
    })

