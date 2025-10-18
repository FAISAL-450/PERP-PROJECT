# A - Import Required Modules
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from .models import JournalEntry
from .forms import JournalEntryForm

# B - Filtering Function
def filter_journalentries(query=None):
    queryset = JournalEntry.objects.all()
    if query:
        queryset = queryset.filter(
            Q(description__icontains=query) |
            Q(debit_account__account_name__icontains=query) |
            Q(credit_account__account_name__icontains=query)
        )
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
def journalentry_dashboard(request):
    query = request.GET.get("q", "").strip()
    journalentries = filter_journalentries(query)
    journalentries_page = get_paginated_queryset(request, journalentries, per_page=10)

    form = JournalEntryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        entry = form.save(commit=False)
        entry.save()
        messages.success(request, "✅ Journal Entry created successfully.")
        return redirect(f"{reverse('journalentry_dashboard')}?q={query}")

    return render(request, "journalentry/journalentry_dashboard.html", {
        "journalentries": journalentries_page,
        "query": query,
        "form": form,
        "mode": "list"
    })

# E - Edit View (Inline Form + List Table)
def edit_journalentry(request, pk):
    journalentry = get_object_or_404(JournalEntry, pk=pk)
    query = request.GET.get("q", "").strip()

    form = JournalEntryForm(request.POST or None, instance=journalentry)
    if form.is_valid():
        form.save()
        messages.success(request, "✏️ Journal Entry updated successfully.")
        return redirect(f"{reverse('journalentry_dashboard')}?q={query}")

    journalentries = filter_journalentries(query)
    journalentries_page = get_paginated_queryset(request, journalentries, per_page=10)

    return render(request, "journalentry/journalentry_dashboard.html", {
        "form": form,
        "mode": "edit",
        "journalentry": journalentry,
        "query": query,
        "journalentries": journalentries_page
    })

# F - Delete View (Confirmation + Redirect)
def journalentry_delete(request, pk):
    journalentry = get_object_or_404(JournalEntry, pk=pk)
    query = request.GET.get("q", "").strip()

    if request.method == 'POST':
        name = journalentry.date
        journalentry.delete()
        messages.success(request, f"🗑️ Journal Entry dated '{name}' deleted successfully.")
        return redirect(f"{reverse('journalentry_dashboard')}?q={query}")


