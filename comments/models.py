from django.conf import settings
from django.db import models

from blog.models import BaseModel, Article


class Comment(BaseModel):
  body = models.TextField('body', max_length=300)
  author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      verbose_name='author',
      on_delete=models.CASCADE,
  )
  article = models.ForeignKey(
      Article,
      verbose_name='article',
      on_delete=models.CASCADE,
  )
  parent_comment = models.ForeignKey(
      'self',
      verbose_name='parent comment',
      blank=True,
      null=True,
      on_delete=models.CASCADE,
  )

  class Meta:
    ordering = ['-id']
    verbose_name = 'comment'
    verbose_name_plural = 'comments'

  def __str__(self):
    return self.body
