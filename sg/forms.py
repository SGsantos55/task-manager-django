from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Todo

class createtodo(ModelForm):
    class Meta:
        model=Todo
        fields = ['title','description','completed']
