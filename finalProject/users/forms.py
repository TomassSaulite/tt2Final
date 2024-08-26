from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    usable_password = None
    help_texts = None
    email = forms.EmailField(max_length=200, help_text=None)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['isClient'].label = "Are you a Client?"  # Change the label
        self.fields['isRestaurant'].label = "Are you a Restaurant?"
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password1','password2', 'isClient', 'isRestaurant')
        # fields = ( 'email', 'username', 'password1','password2')
    # Custom validation to ensure only one checkbox is selected
    def clean(self):
        cleaned_data = super().clean()
        is_client = cleaned_data.get('isClient')
        is_restaurant = cleaned_data.get('isRestaurant')

        # Ensure that only one checkbox is selected
        if is_client and is_restaurant:
            raise forms.ValidationError("You can only select either 'Client' or 'Restaurant', not both.")
        if not is_client and not is_restaurant:
            raise forms.ValidationError("You must select either 'Client' or 'Restaurant'.")

        return cleaned_data

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
        
        