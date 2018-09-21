# coding: utf-8
from m3_ext.context_processors import DesktopProcessor


def desktop(request):
    u"""Подготавливает данные для шаблона HTML-страницы с рабочим столом."""
    return DesktopProcessor.process(request)
