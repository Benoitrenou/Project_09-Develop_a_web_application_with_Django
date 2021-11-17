from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models

@login_required
def home(request):
    return render (request, 'reviews/home.html')
