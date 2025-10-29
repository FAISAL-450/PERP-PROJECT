from django.contrib import admin
from .models import Profile, CustomerDetailed

# 🔐 Azure Admin Email
AZURE_ADMIN_EMAIL = 'admin@dzignscapeprofessionals.onmicrosoft.com'

class AzureAdminOnlyMixin:
    def has_module_permission(self, request):
        return request.user.email == AZURE_ADMIN_EMAIL

    def has_view_permission(self, request, obj=None):
        return request.user.email == AZURE_ADMIN_EMAIL

    def has_change_permission(self, request, obj=None):
        return request.user.email == AZURE_ADMIN_EMAIL

    def has_delete_permission(self, request, obj=None):
        return request.user.email == AZURE_ADMIN_EMAIL

@admin.register(Profile)
class ProfileAdmin(AzureAdminOnlyMixin, admin.ModelAdmin):
    list_display = ['user', 'role']
    list_filter = ['role']
    search_fields = ['user__username']

@admin.register(CustomerDetailed)
class CustomerDetailedAdmin(AzureAdminOnlyMixin, admin.ModelAdmin):
    list_display = ['name', 'company', 'created_by', 'team', 'created_at']
    list_filter = ['team', 'created_by']
    search_fields = ['name', 'company', 'created_by__username']


