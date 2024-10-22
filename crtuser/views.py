from django.shortcuts import render
from .forms import CreateUser, LoginForm

def show_form_register(request):
    form = CreateUser()
    return render(request=request, template_name='register.html',context={'form':form})

def validate_user_creation():...



def show_form_login(request):
    form = LoginForm()
    return render(request=request, template_name='login.html',context={'login_form':form})

def validate_login():...