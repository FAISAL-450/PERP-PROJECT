from django.urls import path
from . import views
app_name = 'lead'

urlpatterns = [
    path('lead-details/', views.salesmarketing_ld_list, name='salesmarketing_ld_list'),
    path('customerdetailed-details/', views.salesmarketing_doc_list, name='salesmarketing_doc_list'),

]

