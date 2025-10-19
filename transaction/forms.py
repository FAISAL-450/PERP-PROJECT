from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'transaction_type',
            'reference',
            'description',
            'amount',
            'date',
            'debit_account',
            'credit_account',
            'status',
        ]

        labels = {
            'transaction_type': 'Transaction Type',
            'reference': 'Reference No.',
            'description': 'Description',
            'amount': 'Amount',
            'date': 'Transaction Date',
            'debit_account': 'Debit Account',
            'credit_account': 'Credit Account',
            'status': 'Status',
        }

        widgets = {
            'transaction_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select transaction type'
            }),
            'reference': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter reference number'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'Enter transaction description'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'debit_account': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select debit account'
            }),
            'credit_account': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select credit account'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select status'
            }),
        }
