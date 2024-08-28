from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required(redirect_field_name=None)
def extraClientInfo(request):
  return render(request, 'client/extraClientInfo.html')

