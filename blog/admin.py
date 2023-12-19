from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Article


admin.site.register(Article)