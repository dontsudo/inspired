from django.urls import path
from django.urls import re_path

from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    re_path(r'^login/$',
            views.LoginView.as_view(form_class=LoginForm),
            name='login'),
    re_path(r'^register/$',
            views.RegisterView.as_view(),
            name='register'),
]
