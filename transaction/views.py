# A - Import Required Modules
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm

# B - Filtering Function
def filter_transactions(query=None):
    queryset = Transaction.objects.all()
    if query:
        queryset = queryset.filter(Q(status__icontains=query))
    return queryset

# C - Reusable Pagination Function
def get_paginated_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")

    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

# D - Unified View (List View + Form Submission)
def transaction_dashboard(request):
    query = request.GET.get("q", "").strip()
    transactions = filter_transactions(query)
    transactions_page = get_paginated_queryset(request, transactions, per_page=10)

    form = TransactionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        transaction = form.save(commit=False)
        transaction.save()
        messages.success(request, "✅ Transaction created successfully.")
        return redirect(f"{reverse('transaction_dashboard')}?q={query}")

    return render(request, "transaction/transaction_dashboard.html", {
        "transactions": transactions_page,
        "query": query,
        "form": form,
        "mode": "list"
    })

# E - Edit View (Inline Form + List Table)
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    query = request.GET.get("q", "").strip()

    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        messages.success(request, "✏️ Transaction updated successfully.")
        return redirect(f"{reverse('transaction_dashboard')}?q={query}")

    transactions = filter_transactions(query)
    transactions_page = get_paginated_queryset(request, transactions, per_page=10)

    return render(request, "transaction/transaction_dashboard.html", {
        "form": form,
        "mode": "edit",
        "transaction": transaction,
        "query": query,
        "transactions": transactions_page
    })

# F - Delete View (Confirmation + Redirect)
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    query = request.GET.get("q", "").strip()

    if request.method == 'POST':
        status = transaction.status
        transaction.delete()
        messages.success(request, f"🗑️ Transaction '{status}' deleted successfully.")
        return redirect(f"{reverse('transaction_dashboard')}?q={query}")
