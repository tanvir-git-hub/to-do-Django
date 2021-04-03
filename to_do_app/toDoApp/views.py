from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    form = UserCreationForm()
    return render(request, 'todoapp/index.html', {"form":form})

def signup(request):
    
    return render(request, 'todoapp/profile.html')

    
