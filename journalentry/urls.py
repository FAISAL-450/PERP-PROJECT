from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.journalentry_dashboard, name='journalentry_dashboard'),
    path('dashboard/edit/<int:pk>/', views.edit_journalentry, name='edit_journalentry'),
    path('dashboard/delete/<int:pk>/', views.journalentry_delete, name='journalentry_delete'),
]
