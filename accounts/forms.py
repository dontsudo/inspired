from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super(LoginForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget = widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    })
    self.fields['password'].widget = widgets.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    })


class RegisterForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super(RegisterForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget = widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    })
    self.fields['email'].widget = widgets.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email'
    })
    self.fields['password1'].widget = widgets.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    })
    self.fields['password2'].widget = widgets.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'repeat password'
    })

  def clean_email(self):
    email = self.cleaned_data['email']
    if get_user_model().objects.filter(email=email).exists():
      raise ValidationError(_('email already exists'))

    return email

  class Meta:
    model = get_user_model()
    fields = ('username', 'email')
