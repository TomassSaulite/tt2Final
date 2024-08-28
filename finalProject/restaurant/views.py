from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required(redirect_field_name=None)
def extraRestaurantInfo(request):
  return render(request, 'restaurant/extraRestaurantInfo.html')