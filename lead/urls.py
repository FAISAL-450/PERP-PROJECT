from django.urls import path
from . import views

urlpatterns = [
    # 🔹 Team dashboard: Nayan & Salim manage their own leads
    path('dashboard/', views.lead_dashboard, name='lead_dashboard'),

    # 🔹 Admin dashboard: Kamal views all lead records (read-only)
    path('dashboard/admin/', views.lead_admin_dashboard, name='lead_admin_dashboard'),

    # ✏️ Edit lead entry (only owner can edit)
    path('dashboard/edit/<int:pk>/', views.edit_lead, name='edit_lead'),

    # 🗑️ Delete lead entry (only owner can delete)
    path('dashboard/delete/<int:pk>/', views.lead_delete, name='lead_delete'),
    
    

]

