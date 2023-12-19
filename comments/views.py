from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView

from .forms import CommentForm
from .models import Comment


class CommentPostView(FormView):
  form_class = CommentForm
  template_name = 'blog/article_detail.html'

  @method_decorator(csrf_protect)
  def dispatch(self, request, *args, **kwargs):
    return super(CommentPostView, self).dispatch(request, *args, **kwargs)
