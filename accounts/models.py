from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogUser(AbstractUser):
  
  nickname = models.CharField(_('nickname'), max_length=20)
  created_time = models.DateTimeField(_('created time'), auto_now_add=True)
  updated_time = models.DateTimeField(_('updated time'), auto_now=True)

  def __str__(self):
    return self.email

  class Meta:
    ordering = ['-id']
    verbose_name = _('user')
    verbose_name_plural = verbose_name
    get_latest_by = 'id'
