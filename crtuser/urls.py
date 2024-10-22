from django.urls import path
from .views import show_form_register, validate_user_creation, show_form_login,validate_login

app_name = 'ct_hash'
urlpatterns = [
    path('', show_form_register, name='home_register'),
    path('create/hash/', validate_user_creation, name='create_hash'),
    path('login/', show_form_login, name='home_login'),
    path('login/hash/', validate_login, name='login_hash'),
]
