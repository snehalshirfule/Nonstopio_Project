from dataclasses import field
from itertools import product
from pyexpat import model
from django import forms
from .models import user,products

class UserForm(forms.ModelForm):
    class Meta:
        model= user
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = "__all__"

