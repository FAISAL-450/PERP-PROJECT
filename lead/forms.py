from django import forms
from .models import Lead
from customerdetailed.models import CustomerDetailed

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'customer_company',
            'source',
            'status',
            'notes',
        ]
        labels = {
            'customer_name': 'Customer Name',
            'customer_email': 'Email Address',
            'customer_phone': 'Phone Number',
            'customer_company': 'Company Name',
            'source': 'Lead Source',
            'status': 'Lead Status',
            'notes': 'Additional Notes',
        }
        widgets = {
            'customer_name': forms.Select(attrs={
                'class': 'form-control',
            }),
            'customer_email': forms.TextInput(attrs={
                'class': 'form-control input-light-green',
                'readonly': 'readonly',
                'placeholder': 'Auto-filled from customer name'
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control input-light-green',
                'readonly': 'readonly',
                'placeholder': 'Auto-filled from customer name'
            }),
            'customer_company': forms.TextInput(attrs={
                'class': 'form-control input-light-green',
                'readonly': 'readonly',
                'placeholder': 'Auto-filled from customer name'
            }),
            'source': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'Enter any notes'
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Injected from view
        super().__init__(*args, **kwargs)

        self.fields['customer_name'].empty_label = "--------- Select Customer Name ---------"

        # Filter customer_name based on logged-in user
        if user and user.username in ['belal', 'emon']:
            self.fields['customer_name'].queryset = CustomerDetailed.objects.filter(created_by=user)
        else:
            self.fields['customer_name'].queryset = CustomerDetailed.objects.none()
