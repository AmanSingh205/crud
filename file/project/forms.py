from django import forms
from .models import User
class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','age']
        