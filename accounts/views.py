from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView

from .forms import LoginForm, RegisterForm


class LoginView(FormView):
  form_class = LoginForm
  template_name = 'accounts/login.html'
  success_url = '/'
  redirect_field_name = REDIRECT_FIELD_NAME

  

class RegisterView(FormView):
  form_class = RegisterForm
  template_name = 'accounts/register.html'
  success_url = '/'

  def form_valid(self, form: RegisterForm):
    if form.is_valid():
      form.save()  # save user

      # TODO: send email here

    return super().form_valid(form)
