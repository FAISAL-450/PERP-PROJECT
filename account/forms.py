from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'name',
            'code',
            'type',
            'description',
            'is_active',
            'currency',
            'cost_center',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Account Name',
                'class': 'form-control',
                'autofocus': 'autofocus'
            }),
            'code': forms.TextInput(attrs={
                'placeholder': 'e.g. ACC-1001',
                'class': 'form-control'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Optional description',
                'class': 'form-control'
            }),
            'currency': forms.TextInput(attrs={
                'placeholder': 'e.g. USD',
                'class': 'form-control'
            }),
            'cost_center': forms.TextInput(attrs={
                'placeholder': 'e.g. Marketing, IT',
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_code(self):
        code = self.cleaned_data['code']
        return code.upper().strip()
