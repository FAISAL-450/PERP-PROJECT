from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.transaction_dashboard, name='transaction_dashboard'),         # ✅ List + Create
    path('dashboard/edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),     # ✅ Edit by primary key
    path('dashboard/delete/<int:pk>/', views.transaction_delete, name='transaction_delete') # ✅ Delete by primary key
]
