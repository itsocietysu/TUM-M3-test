# coding:utf-8
# pylint: disable=function-redefined
from django.apps.config import AppConfig


class AppConfig(AppConfig):

    name = __package__
