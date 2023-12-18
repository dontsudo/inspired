from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.generic import FormView, RedirectView

from .forms import LoginForm, RegisterForm


class LoginView(RedirectView):

  form_class = LoginForm
  template_name = 'accounts/login.html'
  success_url = '/'

  def form_valid(self, form: LoginForm):
    form = AuthenticationForm(data=self.request.POST, request=self.request)
    if form.is_valid():
      auth.login(self.request, form.get_user())

    return super().form_valid(form)


class RegisterView(FormView):

  form_class = RegisterForm
  template_name = 'accounts/register.html'

  def form_valid(self, form: RegisterForm):
    if form.is_valid():
      form.save()  # save user

      # TODO: send email here

    return super().form_valid(form)
