# coding: utf-8
from django.conf.urls import url

from m3demo.core.controllers import main_controller


def register_urlpatterns():
    u"""Регистрация URL'ов приложения."""
    main_urlpattern = main_controller.urlpattern

    return [
        url(r'^$', main_controller.process_request),
        url(*main_urlpattern),
    ]
