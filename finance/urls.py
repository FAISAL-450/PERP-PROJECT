from django.urls import path
from . import views
app_name = 'finance'  # Namespace for reverse URL resolution
urlpatterns = [
    path('account-detailed/', views.finance_ac_list, name='finance_ac_list'),
    path('journalentry-detailed/', views.finance_je_list, name='finance_je_list'),
]
