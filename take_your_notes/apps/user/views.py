from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.generic import View, FormView
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.conf import settings
from .forms import SignUpForm, SignInForm


class GuestView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)
class SignUpView(FormView, GuestView):
    form_class = SignUpForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('core:home')
    def form_valid(self, form):
        request = self.request
        user = form.save()
        user = authenticate(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password1'])
        login(request,user)
        messages.success(request, _('You are successfully signed up!'))
        return super(SignUpView,self).form_valid(form)

class SignInView(FormView, GuestView):
    form_class = SignInForm
    template_name = 'user/signin.html'
    success_url = reverse_lazy('core:home')
    def form_valid(self, form):
        request = self.request
        login(request, form.user_cache)
        return super(SignInView, self).form_valid(form)
