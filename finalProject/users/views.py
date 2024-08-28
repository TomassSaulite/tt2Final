from .forms import SignupForm
from .forms import CustomLoginForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.http import Http404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


def index(request):
  template = loader.get_template('users/index.html')
  return HttpResponse(template.render())


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)                         
            return redirect('loginSuccessful')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def custom_login_view(request):
    form = CustomLoginForm(request=request, data=request.POST or None)
    # return redirect(next_url)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()  # Fetch the authenticated user
            if user:
                auth_login(request, user)  # Correct usage of login() function
                return redirect('loginSuccessful')  # Replace 'home' with your desired success URL
    return render(request, 'users/login.html', {'form': form})

# @login_required(redirect_field_name=None)
def loginSuccessful(request):
    isClient = request.user.isClient
    isClient=int(isClient)
    print(123)
    return render(request, 'users/loginSuccessful.html', {"isClient": isClient})


from django.contrib.auth import logout as logouts

# @login_required(redirect_field_name=None)
def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('index')
