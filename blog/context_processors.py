"""
context_processors

- 전역 변수를 템플릿에서 사용할 수 있도록 해주는 함수
- settings.py의 TEMPLATES의 context_processors에 등록해야 함
"""

import logging

from django.core.cache import cache
from django.http import HttpRequest

logger = logging.getLogger(__name__)


def seo_processor(request: HttpRequest):
  key = 'seo_processor'
  value = cache.get(key)

  if value:
    return value

  logger.info('🍜 SEO PROCESSOR: cache miss')
  value = {
    'SITE_NAME': 'inspired',
    'SITE_SEO_DESCRIPTION': 'blog for developers.',
    'SITE_DESCRIPTION': 'blog for developers.',
    'SITE_KEYWORDS': 'inspired, blog, developer',
    'SITE_BASE_URL': request.scheme + '://' + request.get_host() + '/',
  }
  cache.set(key, value, 60 * 60 * 10)

  return value
