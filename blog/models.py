from django.conf import settings
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
  author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      verbose_name=_('author'),
      blank=False,
      null=False,
      on_delete=models.CASCADE,
  )
  category = models.ForeignKey(
      'Category',
      verbose_name=_('category'),
      blank=True,
      null=True,
      on_delete=models.CASCADE,
  )
  tags = models.ManyToManyField('Tag', verbose_name=_('tags'), blank=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_time']
    verbose_name = _('article')
    verbose_name_plural = _('articles')

  def viewed(self):
    self.views += 1
    self.save(update_fields=['views'])


class Category(BaseModel):
  name = models.CharField(_('category name'), max_length=50, unique=True)
  parent_category = models.ForeignKey(
      'self',
      verbose_name=_('parent category'),
      blank=True,
      null=True,
      on_delete=models.CASCADE,
  )
  slug = models.SlugField(default='no-slug', max_length=60, blank=True)
  index = models.IntegerField(default=0, verbose_name=_('index'))

  class Meta:
    ordering = ['-index']
    verbose_name = _('category')
    verbose_name_plural = _('categories')

  def __str__(self):
    return self.name


class Tag(BaseModel):
  name = models.CharField(_('tag name'), max_length=50, unique=True)
  slug = models.SlugField(default='no-slug', max_length=60, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']
    verbose_name = _('tag')
    verbose_name_plural = _('tags')
