from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def extraRestaurantInfo(request):
  template = loader.get_template('restaurant/extraRestaurantInfo.html')
  return HttpResponse(template.render())
