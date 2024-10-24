from django.shortcuts import render, redirect
from .forms import CreateUser, LoginForm
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login

def show_form_register(request):
    session_ = request.session.get('user_session',{})
    form = CreateUser(session_)
    return render(request=request, template_name='register.html',context={'form':form})

@require_POST
def validate_user_creation(request):
    do_post = request.POST
    session_ = request.session['user_session'] = do_post
    form_instance = CreateUser(do_post)
    print(form_instance)
    if form_instance.is_valid():
        user = form_instance.save(commit=False)
        user.set_password(user.password)
        user.save()
    else:
        form_instance = CreateUser()
    return redirect('ct_hash:home_login')


def show_form_login(request):
    form = LoginForm()
    return render(request=request, template_name='login.html',context={'login_form':form})

@require_POST
def validate_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request,username,password)
    if user is not None:
        login(request=request, user=user)
        return redirect('ecommer:ecommer_home')
    else:
        'Retorna uma mensagem de erro caso o login esteja inválido'
    return redirect('ct_hash:home_login')