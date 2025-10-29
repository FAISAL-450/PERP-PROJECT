from django.shortcuts import render
from customerdetailed.models import CustomerDetailed
from lead.models import Lead
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

# 💼 Sales & Marketing Customer Detailed View
def salesmarketing_doc_list(request):
    query = request.GET.get('q', '').strip()
    customerdetaileds = CustomerDetailed.objects.all()
    if query:
        customerdetaileds = customerdetaileds.filter(name__icontains=query)

    customerdetaileds_page = get_paginated_queryset(request, customerdetaileds, per_page=10)

    return render(request, 'salesmarketing/salesmarketing_doc_list.html', {
        'customerdetaileds': customerdetaileds_page,
        'query': query
    })

# 💼 Sales & Marketing Lead Detailed View
def salesmarketing_ld_list(request):
    query = request.GET.get('q', '').strip()
    leads = Lead.objects.all()
    if query:
        leads = leads.filter(customer_name__icontains=query)

    leads_page = get_paginated_queryset(request, leads, per_page=10)

    return render(request, 'salesmarketing/salesmarketing_ld_list.html', {
        'leads': leads_page,
        'query': query
    })

