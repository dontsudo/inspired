import time

from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


class ArticleListView(ListView):
  model = Article
  context_object_name = 'article_list'
  template_name = 'blog/article_index.html'

  def get_queryset(self) -> QuerySet[Any]:
    time.sleep(3)

    return Article.objects.filter(
        created_time__lte=timezone.now()).order_by('-created_time')


class IndexView(ArticleListView):
  paginate_by = 10

  def get_queryset(self):
    return super().get_queryset().filter(created_time__lte=timezone.now())


class ArticleDetailView(DetailView):
  model = Article
  context_object_name = 'article'
  template_name = 'blog/article_detail.html'
