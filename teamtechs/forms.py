from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [ 'username', 'email', 'message' ]