from django.urls import path
from . import views
app_name = 'construction'
urlpatterns = [
    path('project-detailed/', views.construction_pd_list, name='construction_pd_list'),
    
]
