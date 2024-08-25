from django.template import loader
from django.http import HttpResponse

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})