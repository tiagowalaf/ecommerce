from django.shortcuts import render
from .forms import CreateUser

def show_form_register(request):
    form = CreateUser()
    return render(request=request, template_name='register.html',context={'form':form})

def validate_user_creation():...



def show_form_login(request):
    return render(request=request, template_name='login.html')

def validate_login():...