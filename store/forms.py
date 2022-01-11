from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Category,Brand, Product
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
   
    

    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']



class ProductForm(ModelForm):
   class Meta:
        model = Product
        fields = ['category', 'brand', 'name', 'price', 'digital', 'image']