# coding: utf-8
from inspect import isclass

from educommon.m3 import get_pack
from m3.actions import ActionPack


def get_fullname(last_name, first_name, middle_name=None):
    u"""Возвращает ФИО полностью по фамилии, имени и отчеству.

    :param unicode last_name: Фамилия.

    :param unicode first_name: Имя.

    :param middle_name: Отчество.
    :type middle_name: unicode or NoneType

    :rtype: unicode
    """
    return u' '.join(
        name.capitalize()
        for name in (last_name, first_name, middle_name)
        if name
    )


class ModelRegister(object):

    u"""Реестр соответствия моделей и наборов действий.

    Подменяет наборы действий из :var:`m3demo.core.controllers.core_observer`
    на наборы из словаря :arg:`register`.
    """

    def __init__(self, register, base_register):
        u"""Инициализация экземпляра реестра.

        :param dict register: словарь соответствия моделей и наборов действий.

        :param base_register: базовый реестр.
        :type: objectpack.observer.base.Observer
        """
        self.base_register = base_register
        self.register = register

    def get(self, model_name):
        u"""Возвращает набор действий для модели :arg:`model_name`.

        :param str model_name: имя класса модели.

        :rtype: m3.actions.ActionPack
        """
        pack = self.register.get(model_name)

        if (
            isinstance(pack, basestring) or
            isclass(pack) and issubclass(pack, ActionPack)
        ):
            pack = get_pack(pack)

        return pack or self.base_register.get(model_name)
