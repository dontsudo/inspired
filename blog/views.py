from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


class ArticleListView(ListView):
  model = Article
  context_object_name = 'article_list'
  queryset = Article.objects.all()
  template_name = 'blog/article_index.html'


class IndexView(ArticleListView):
  paginate_by = 10

  def get_queryset(self):
    return super().get_queryset().filter(created_time__lte=timezone.now())


class ArticleDetailView(DetailView):
  model = Article
  context_object_name = 'article'
  template_name = 'blog/article_detail.html'
