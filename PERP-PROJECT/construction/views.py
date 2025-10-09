from django.shortcuts import render
from project.models import Project
from django.core.paginator import Paginator

def construction_pd_list(request):
    query = request.GET.get('q', '')
    projects = Project.objects.filter(department='construction')
    if query:
        projects = projects.filter(name_of_project__icontains=query)

    paginator = Paginator(projects, 10)  # Show 10 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'construction/construction_pd_list.html', {
        'projects': page_obj,
        'query': query
    })


