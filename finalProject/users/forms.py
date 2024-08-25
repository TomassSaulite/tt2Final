from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    usable_password = None
    help_texts = None
    email = forms.EmailField(max_length=200, help_text=None)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].label = 'password1 label'
        # self.fields['password2'].label = 'password2 label'

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    class Meta:
        model = User
        fields = ( 'email', 'password1','password2')

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(self.request, email=email, password=password)
            if self.user is None:
                raise forms.ValidationError('Invalid email or password')
        return self.cleaned_data

    def get_user(self):
        return self.user
        
        