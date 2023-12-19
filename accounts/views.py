from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, RedirectView

from .forms import LoginForm, RegisterForm


class LoginView(FormView):
  form_class = LoginForm
  template_name = 'accounts/login.html'
  success_url = '/'
  redirect_field_name = REDIRECT_FIELD_NAME

  @method_decorator(csrf_protect)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form: LoginForm):
    if form.is_valid():
      print('🤔 form is valid')
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = auth.authenticate(self.request,
                               username=username,
                               password=password)

      if user is not None:
        auth.login(self.request, user)
        return super().form_valid(form)

    return super().form_invalid(form)


class RegisterView(FormView):
  form_class = RegisterForm
  template_name = 'accounts/register.html'
  success_url = '/'

  @method_decorator(csrf_protect)
  def form_valid(self, form: RegisterForm):
    if form.is_valid():
      form.save()  # save user

      # TODO: send email here

    return super().form_valid(form)


class LogoutView(RedirectView):
  url = '/accounts/login/'

  def get(self, request, *args, **kwargs):
    auth.logout(request)
    return super(LogoutView, self).get(request, *args, **kwargs)