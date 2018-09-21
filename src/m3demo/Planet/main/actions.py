# coding: utf-8
from educommon.m3 import PackValidationMixin
from objectpack.actions import ObjectPack

from ..models import Planet
from .ui import EditWindow


class Pack(PackValidationMixin, ObjectPack):

    model = Planet
    _is_primary_for_model = False

    columns = (
        dict(
            data_index='name',
            header=u'Name',
            sortable=True,
            searchable=True,
        ),
    )

    list_sort_order = ('name',)

    add_window = edit_window = EditWindow

    def extend_desktop(self, menu):
        u"""Возвращает ярлык для рабочего стола."""
        return menu.Item(self.title, self, icon='planets')

    def extend_menu(self, menu):
        u"""Возвращает ярлык для меню "Пуск"."""
        return menu.administry(
            menu.Item(self.title, self),
        )