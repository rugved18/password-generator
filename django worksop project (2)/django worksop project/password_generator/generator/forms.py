# In forms.py of your Django app (e.g., app1)
from django import forms

class PasswordSaveForm(forms.Form):
    service = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.HiddenInput)
