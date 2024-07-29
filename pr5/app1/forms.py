from django import forms

class dataform(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255)
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class studentloginform(AuthenticationForm):
    username = forms.EmailField(label='Email')
