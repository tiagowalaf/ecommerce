from django.shortcuts import render

def show_form_register(request):
    return render(request=request, template_name='register.html')


def show_form_login(request):
    return render(request=request, template_name='login.html')