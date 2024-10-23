from django.shortcuts import render
from .forms import CreateUser, LoginForm
from django.views.decorators.http import require_POST

def show_form_register(request):
    session_ = request.session.get('user_session',{})
    form = CreateUser(session_)
    return render(request=request, template_name='register.html',context={'form':form})

@require_POST
def validate_user_creation(request):...




def show_form_login(request):
    form = LoginForm()
    return render(request=request, template_name='login.html',context={'login_form':form})

@require_POST
def validate_login():...