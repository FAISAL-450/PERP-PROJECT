from django.urls import path
from . import views
app_name = 'design'

urlpatterns = [
    path('client-detailed/', views.design_cd_list, name='design_cd_list'),
]

