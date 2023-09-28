from django import forms
from main.models import Motors
from django.contrib.auth.models import User




class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
         
        widgets={
        "username":forms.TextInput(attrs={"class":"form-control"}),
        "email":forms.EmailInput(attrs={"class":"form-control"}),
        "password":forms.PasswordInput(attrs={"class":"form-control"})
     }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class MotorCreateForm(forms.ModelForm):
    class Meta:
        model=Motors
        fields="__all__"
        
        widgets={
        "name":forms.TextInput(attrs={"class":"form-control"}),
        "model":forms.TextInput(attrs={"class":"form-control"}),
        "company":forms.TextInput(attrs={"class":"form-control"}),
        "mileage":forms.TextInput(attrs={"class":"form-control"})
     }