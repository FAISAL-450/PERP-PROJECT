from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from project.models import Project
from customer.models import Client

@login_required
def home_view(request):
    # Safely get user email or fallback to username
    user_email = getattr(request.user, "email", request.user.username).lower()

    # 📦 Project Summary
    total_projects = Project.objects.count()
    project_names = list(
        Project.objects.order_by("name_of_project").values_list("name_of_project", flat=True)
    )

    # 🧑‍💼 Client Summary
    total_clients = Client.objects.count()
    client_names = list(
        Client.objects.order_by("client_name").values_list("client_name", flat=True)
    )

    # Context passed to the template
    context = {
        "user_email": user_email,
        "total_projects": total_projects,
        "project_names": project_names,
        "total_clients": total_clients,
        "client_names": client_names,
    }

    # Render the homepage with context
    return render(request, "home/home.html", context)


