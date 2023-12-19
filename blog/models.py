from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
  id = models.AutoField(primary_key=True)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Article(BaseModel):
  title = models.CharField(_('title'), max_length=200)
  body = models.TextField(_('body'))
  views = models.PositiveIntegerField(_('views'), default=0)

  class Meta:
    ordering = ['-created_time']
    verbose_name = _('article')
    verbose_name_plural = _('articles')

  def viewed(self):
    self.views += 1
    self.save(update_fields=['views'])