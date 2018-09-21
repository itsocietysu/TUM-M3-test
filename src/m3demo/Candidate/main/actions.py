# coding: utf-8
from educommon.m3 import PackValidationMixin
from objectpack.actions import ObjectPack

from ..models import Candidate
from .ui import EditWindow


class Pack(PackValidationMixin, ObjectPack):

    model = Candidate
    _is_primary_for_model = False

    columns = (
        dict(
            data_index='name',
            header=u'Name',
            sortable=True,
            searchable=True,
        ),
        dict(
            data_index='age',
            header=u'Age',
        ),
        dict(
            data_index='email',
            header=u'Email',
        ),
        dict(
            data_index='planet',
            header=u'Planet',
        ),
        dict(
            data_index='jedi',
            header=u'Jedi',
        ),
    )

    list_sort_order = ('name',)

    add_window = edit_window = EditWindow

    def extend_desktop(self, menu):
        u"""Возвращает ярлык для рабочего стола."""
        return menu.Item(self.title, self, icon='candidates')

    def extend_menu(self, menu):
        u"""Возвращает ярлык для меню "Пуск"."""
        return menu.administry(
            menu.Item(self.title, self),
        )
