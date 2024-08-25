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
        help_texts = { 'username': None, 'email': None,'password1': None, 'password2': None,'password':None }