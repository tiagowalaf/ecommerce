from django.shortcuts import render

def ecommer_home(request):
    return render(request, 'inicio.html')