# coding: utf-8
from django.dispatch.dispatcher import receiver
from educommon.m3 import get_pack
from objectpack.desktop import uificate_the_controller

from m3demo.core.controllers import main_controller

from .actions import DesktopPack


@receiver(main_controller.populate_redirect_map)
def _populate_map(sender, redirect_map, **kwargs):
    u"""Назначает адресу "/" путь к обработчику, формирующему рабочий стол."""
    url = '/'
    assert url not in redirect_map, redirect_map
    pack = get_pack(DesktopPack)
    redirect_map[url] = pack.desktop_action.get_absolute_url()


def register_actions():
    u"""Регистрирует наборы действий приложения в M3."""
    main_controller.extend_packs((
        DesktopPack(),
    ))


def register_desktop_menu():
    u"""Выполняет добавление ярлыков из наборов действий.

    Ярлыки определяются с помощью методов :meth:`extend_desktop` и
    :meth:`extend_menu`.
    """
    uificate_the_controller(main_controller)
