from typing import Any
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomerChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomerChangeForm
  model = CustomUser

  list_display = ('email',)



admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.unregister(Group)
