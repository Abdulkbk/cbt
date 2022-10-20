from typing import List
from datetime import datetime as dt
from unicodedata import name
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create your models here.
class UserManager(BaseUserManager):

  def create_user(self, email, password, name, **extra_fields):

    if not email:
      raise ValueError("Email is required")
    
    if not name:
      raise ValueError("Name is required")

    user = self.model(
      email = self.normalize_email(email),
      name = name,
      **extra_fields,
    )

    user.set_password(password)

    user.save()

    return user

  
  def create_superuser(self, email, password, name, **extra_fields):

    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    return self.create_user(email, password, name, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):

  email: str = models.EmailField(verbose_name='email address', unique=True, max_length=255)
  username: str = models.CharField(verbose_name='username', unique=True, max_length=50,)
  name: str = models.CharField(max_length=255)
  date_joined = models.DateTimeField(default = dt.now())
  is_staff: bool = models.BooleanField(default=False)
  is_active: bool = models.BooleanField(default=True)
  is_superuser: bool = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS: List[str] = ['name', 'username']

  objects = UserManager()

  def __str__(self) -> str:
    return self.name
