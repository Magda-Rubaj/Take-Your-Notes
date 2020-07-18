from django import forms
from django.forms import ValidationError
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

class SignInForm(forms.Form):
    email_or_username = forms.CharField(label=_('Email or Username'))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']
        user = User.objects.filter(
            Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('Provided email or username is incorrect'), code='invalid')
        self.user_cache = user
        return email_or_username
    
    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache.check_password(password):
            raise ValidationError(_('You have entered an invalid password.'))

        return password
