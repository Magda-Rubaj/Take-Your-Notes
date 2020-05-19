from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        unique=True, 
        max_length=10, 
        validators=[username_validator],
        error_messages={
            'max_length':"Username must contain max. 10 characters",
            'unique':"User with that username already exists"
            }
        )
    email = models.EmailField(
        _('email address'), 
        unique=True,
        error_messages={
            'unique':"User registered under this email already exists"
            }
        )
    
