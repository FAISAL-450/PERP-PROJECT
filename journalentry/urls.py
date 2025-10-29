from django.urls import path
from .views import journal_dashboard  # ✅ Correct view name
urlpatterns = [
    path('', journal_dashboard, name='journalentry_dashboard'),  # ✅ URL name stays the same
]
