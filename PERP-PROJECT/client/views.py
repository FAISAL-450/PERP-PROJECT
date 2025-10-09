# A - Import Required Modules
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from .models import Client
from .forms import ClientForm

# B - Filtering Function (client_name and project_name based)
def filter_clients(query=None):
    queryset = Client.objects.select_related('project_name').all()
    if query:
        queryset = queryset.filter(
            Q(client_name__icontains=query) |
            Q(project_name__name_of_project__icontains=query)
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
def client_dashboard(request):
    query = request.GET.get("q", "").strip()
    clients = filter_clients(query)
    clients_page = get_paginated_queryset(request, clients, per_page=10)

    form = ClientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        client = form.save(commit=False)
        client.save()
        messages.success(request, "✅ Client created successfully.")
        return redirect(f"{reverse('client_dashboard')}?q={query}")

    return render(request, "client/client_dashboard.html", {
        "clients": clients_page,
        "query": query,
        "form": form,
        "mode": "list"
    })

# E - Edit View (Inline Form + List Table)
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    query = request.GET.get("q", "").strip()

    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        messages.success(request, "✏️ Client updated successfully.")
        return redirect(f"{reverse('client_dashboard')}?q={query}")

    clients = filter_clients(query)
    clients_page = get_paginated_queryset(request, clients, per_page=10)

    return render(request, "client/client_dashboard.html", {
        "form": form,
        "mode": "edit",
        "client": client,
        "query": query,
        "clients": clients_page
    })

# F - Delete View (Confirmation + Redirect)
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    query = request.GET.get("q", "").strip()

    if request.method == 'POST':
        name = client.client_name
        client.delete()
        messages.success(request, f"🗑️ Client '{name}' deleted successfully.")
        return redirect(f"{reverse('client_dashboard')}?q={query}")

    return render(request, "client/client_confirm_delete.html", {
        "client": client,
        "query": query
    })

