# coding: utf-8
# pylint: disable=wildcard-import,unused-wildcard-import
u"""Настройки системы для разработки."""
from ._base import *  # @UnusedWildImport


DEBUG = True


INSTALLED_APPS.insert(0, 'django_extensions')
INSTALLED_APPS.append('m3_dev_utils')
