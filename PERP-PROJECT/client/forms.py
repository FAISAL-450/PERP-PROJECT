from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['project_name', 'client_name', 'client_email', 'client_phone', 'client_address']
        labels = {
            'project_name': 'Project Name',
            'client_name': 'Client Name',
            'client_email': 'Client Email',
            'client_phone': 'Client Phone',
            'client_address': 'Client Address',
        }
        widgets = {
            'project_name': forms.Select(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter client name'}),
            'client_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'client_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'client_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure blank option appears at top of dropdown
        self.fields['project_name'].empty_label = "--------- Select Project ---------"

