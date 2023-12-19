"""
context_processors

- 전역 변수를 템플릿에서 사용할 수 있도록 해주는 함수
- settings.py의 TEMPLATES의 context_processors에 등록해야 함
"""

import logging

from django.core.cache import cache

logger = logging.getLogger(__name__)


def seo_processor(requests):
  key = 'seo_processor'
  value = cache.get(key)

  if value:
    return value

  logger.info('SEO Processor: cache miss')
  value = {}

  return value
