from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = [
            'date',
            'description',
            'debit_account',
            'credit_account',
            'amount',
        ]

        labels = {
            'date': 'Entry Date',
            'description': 'Description',
            'debit_account': 'Debit Account Name',
            'credit_account': 'Credit Account Name',
            'amount': 'Amount',
        }

        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Select date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'Enter description'
            }),
            'debit_account': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select debit account'
            }),
            'credit_account': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select credit account'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
        }
