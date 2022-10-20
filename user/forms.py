from typing import Sequence
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(ModelForm):

  class Meta(UserCreationForm.Meta):
    model = CustomUser
    fields: Sequence[str] = UserCreationForm.Meta.fields


class CustomerChangeForm(ModelForm):

  class Meta:
    model = CustomUser
    fields = UserChangeForm.Meta.fields