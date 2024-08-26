from django.template import loader
from django.http import HttpResponse

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
from django.shortcuts import render

def loginSuccessful(request):
    # user = request.user #the user
    # email = user.email #their email
    # username = user.username #their username
    # template = loader.get_template('loginSuccessful.html')
    return render(request, 'loginSuccessful.html')



from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('loginSuccessful')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomLoginForm

def custom_login_view(request):
    form = CustomLoginForm(request=request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()  # Fetch the authenticated user
            if user:
                auth_login(request, user)  # Correct usage of login() function
                messages.success(request, 'You have successfully logged in.')
                return redirect('loginSuccessful')  # Replace 'home' with your desired success URL

    return render(request, 'login.html', {'form': form})

