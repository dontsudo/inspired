from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView

from accounts.models import BlogUser
from blog.models import Article
from .forms import CommentForm


class CommentPostView(FormView):
  form_class = CommentForm
  template_name = 'blog/article_detail.html'

  @method_decorator(csrf_protect)
  def dispatch(self, request, *args, **kwargs):
    return super(CommentPostView, self).dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    user = self.request.user
    author = BlogUser.objects.get(pk=user.pk)
    article_id = self.kwargs['article_id']
    article = get_object_or_404(Article, pk=article_id)

    comment = form.save(commit=False)
    comment.article = article
    comment.author = author

    # TODO: parent comment
    if form.cleaned_data['parent_comment_id']:
      pass

    comment.save(True)

    return HttpResponseRedirect(
        reverse('blog:detail', args=(article_id,)))
