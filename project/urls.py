from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.project_dashboard, name='project_dashboard'),
    path('dashboard/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('dashboard/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
]



