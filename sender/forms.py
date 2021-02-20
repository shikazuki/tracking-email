from django import forms
from .models import EmailHistory


class EmailHistoryForm(forms.ModelForm):

    class Meta:
        model = EmailHistory
        fields = ['send_to']


