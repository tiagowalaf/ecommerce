from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class CreateUser(forms.ModelForm):
    repeat_email = forms.CharField(
        max_length=100,required=True,widget=forms.EmailInput(
            attrs={'name':'confirmEmail', 'id':'confirmEmail','class':'inputUser', 'placeholder':'Digite seu email novamente'}))

    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username':forms.TextInput(
                attrs={'name':'nome','id':'nome','class':'inputUser','placeholder':'Digite seu nome completo aqui'}),
            'email':forms.EmailInput(
                attrs={'name':'email', 'id':'email','class':'inputUser', 'placeholder':'Digite seu email aqui'}),
            'password':forms.PasswordInput(
                attrs={'name':'password', 'id':'password','class':'inputUser', 'placeholder':'Digite sua senha aqui'}),
        }
    def clean_username(self) -> object:
        data = self.cleaned_data.get('username',{})
        if len(data) < 10:
            raise ValidationError(_("Valor menor que 10", code="invalid")) 
        return data

    def clean(self) -> object:
        data = super().clean()
        email = data.get('email',{})
        repeat_email = data.get('repeat_email',{})
        # add validation for field (email if exists)
        if email != repeat_email:
            raise ValidationError(_("Emails não são iguais"), code="invalid")
        return data
    
    def clean_password(self) -> object:
        data = self.cleaned_data.get('password',{})
        password_validator = RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$',
            message="A senha deve ter pelo menos 8 caracteres, incluindo 1 letra maiúscula e 1 número.")
        try:
            password_validator(data)
        except ValidationError as e:
            raise ValidationError(e.message)
        return data
    
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,required=True,widget=forms.EmailInput(
            attrs={'name':'email', 'id':'email','class':'inputUser', 'placeholder':'Digite seu email aqui'}))
    password = forms.CharField(
        max_length=100,required=True,widget=forms.PasswordInput(
            attrs={'name':'password', 'id':'password','class':'inputUser', 'placeholder':'Digite sua senha aqui'}))
    # add validations