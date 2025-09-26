from django.shortcuts import render
from client.models import Client
from django.core.paginator import Paginator

def design_cd_list(request):
    query = request.GET.get('q', '')
    clients = Client.objects.filter(department='construction')
    if query:
        clients = clients.filter(name_of_client__icontains=query)

    paginator = Paginator(clients, 10)  # Show 10 clients per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'design/design_cd_list.html', {
        'clients': page_obj,
        'query': query
    })

