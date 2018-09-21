# coding: utf-8
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from educommon.utils.ui import local_template
from objectpack.actions import BaseAction
from objectpack.actions import BasePack


class DesktopAction(BaseAction):

    u"""Отображение рабочего стола системы.

    На основе django-шаблона формирует HTML-страницу.
    """

    template_path = local_template('desktop.html')

    def _get_template(self, request, context):
        u"""Возвращает шаблон HTML-страницы с рабочим столом системы.

        :rtype: django.template.Template
        """
        return get_template(self.template_path)

    def _get_template_context(self, request, context):
        u"""Возвращает данные для компиляции шаблона.

        :rtype: django.template.context.RequestContext
        """
        result = {}

        result['debug'] = settings.DEBUG

        return result

    def _render_template(self, request, context):
        u"""Возвращает результат компиляции шаблона HTML-страницы.

        :rtype: unicode
        """
        template = self._get_template(request, context)
        template_context = self._get_template_context(request, context)
        return template.render(template_context, request)

    def _get_desktop(self, request, context):
        u"""Возвращает HTTP-ответ с рабочим столом системы."""
        return HttpResponse(
            content=self._render_template(request, context),
            content_type='text/html',
        )

    def run(self, request, context):
        return self._get_desktop(request, context)


class DesktopPack(BasePack):

    u"""Пак рабочего стола."""

    def __init__(self):
        super(DesktopPack, self).__init__()

        self.desktop_action = DesktopAction()

        self.actions.extend((
            self.desktop_action,
        ))
