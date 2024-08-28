from django import forms
from .models import Client

class customClientSignupForm(forms.Form):
    country = forms.CharField(max_length=50) 
    phoneNum = forms.PositiveIntegerField()
    name = forms.CharField(max_length=25)
    lastName = forms.CharField(max_length=25)
        