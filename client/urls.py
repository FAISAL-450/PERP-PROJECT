from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('edit/<int:pk>/', views.edit_client, name='edit_client'),
    path('delete/<int:pk>/', views.client_delete, name='client_delete'),
]


