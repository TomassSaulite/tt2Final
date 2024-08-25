from django.template import loader
from django.http import HttpResponse

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())