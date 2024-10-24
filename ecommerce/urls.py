from django.urls import path
from .views import ecommer_home

app_name = 'ecommer'
urlpatterns = [
    path('', ecommer_home,  name='ecommer_home')
]
