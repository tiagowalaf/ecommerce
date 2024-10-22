from django import forms
from django.contrib.auth.models import User

class CreateUser(forms.ModelForm):
    username = forms.CharField(
        max_length=25,required=True,widget=forms.TextInput(
            attrs={'name':'nome','id':'nome','class':'inputUser','placeholder':'Digite seu nome completo aqui'}))
    
    email = forms.CharField(
        max_length=100,required=True,widget=forms.EmailInput(
            attrs={'name':'email', 'id':'email','class':'inputUser', 'placeholder':'Digite seu email aqui'}))
    repeat_email = forms.CharField(
        max_length=100,required=True,widget=forms.EmailInput(
            attrs={'name':'confirmEmail', 'id':'confirmEmail','class':'inputUser', 'placeholder':'Digite seu email novamente'}))

    password = forms.CharField(
        max_length=100,required=True,widget=forms.PasswordInput(
            attrs={'name':'password', 'id':'password','class':'inputUser', 'placeholder':'Digite sua senha aqui'}))

    class Meta:
        model = User
        fields = ['username','email','password']


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100,required=True,widget=forms.EmailInput(
            attrs={'name':'email', 'id':'email','class':'inputUser', 'placeholder':'Digite seu email aqui'}))
    password = forms.CharField(
        max_length=100,required=True,widget=forms.PasswordInput(
            attrs={'name':'password', 'id':'password','class':'inputUser', 'placeholder':'Digite sua senha aqui'}))