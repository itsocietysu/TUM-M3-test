# coding: utf-8
from django.dispatch.dispatcher import Signal
from educommon.utils.misc import cached_property
from objectpack.observer.base import ObservableController
from objectpack.observer.base import Observer


class RedirectingController(ObservableController):

    u"""Контроллер с перенаправлением запросов внутри себя.

    В атрибуте ``redirect_map`` содержит список соответствия коротких адресов и
    реальных адресов обработчиков. Предоставляет возможность использования
    "сокращенных" адресов.

    Атрибут ``redirect_map`` заполняется в обработчиках сигнала
    ``populate_redirect_map`` (сигнал создается в экземпляре контроллера).
    """

    def __init__(self, *args, **kwargs):
        self.populate_redirect_map = Signal(
            providing_args=('redirect_map',),
        )

        super(RedirectingController, self).__init__(*args, **kwargs)

    @cached_property
    def redirect_map(self):
        u"""Таблица соответствия адресов и обработчиков.

        Заполняется в приложениях проекта через обработчики сигнала
        ``populate_redirect_map``:

        .. code-block:: python

           from m3demo.core.controllers import main_controller

           @receiver(main_controller.populate_redirect_map)
           def _populate_map(sender, redirect_map):
               url = '/'
               assert url not in redirect_map, redirect_map
               pack = get_pack(DesktopPack)
               redirect_map[url] = pack.desktop_action.get_absolute_url()
        """
        result = {}

        self.populate_redirect_map.send(self, redirect_map=result)

        return result

    def process_request(self, request):
        if request.path in self.redirect_map:
            request.path = self.redirect_map[request.path]

        return super(RedirectingController, self).process_request(request)


core_observer = Observer()

main_controller = RedirectingController(core_observer, '/actions')
# -----------------------------------------------------------------------------
