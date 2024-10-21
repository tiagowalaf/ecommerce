from django.urls import path
from .views import show_form_register, show_form_login

app_name = 'ct_hash'
urlpatterns = [
    path('', show_form_register, name='home_register'),
    path('login/', show_form_login, name='home_login'),
]
