# coding: utf-8
import json

from m3.actions.context import DeclarativeActionContext
from m3.actions.context import _date_parser


def register_dac_parsers():
    u"""Регистрация дополнительных парсеров для параметров контекста."""
    DeclarativeActionContext.register_parser(
        'int_list',
        lambda string: [int(x) for x in string.split(',')] if string else []
    )

    DeclarativeActionContext.register_parser(
        'int_or_none',
        lambda x: int(x) if x else None
    )

    DeclarativeActionContext.register_parser(
        'date_or_none',
        lambda x: _date_parser(x) if x else None
    )

    DeclarativeActionContext.register_parser(
        'int_or_zero',
        lambda x: int(x) if (x or x in [u'0', '0', 0]) else 0
    )

    DeclarativeActionContext.register_parser(
        'int_set_or_none',
        lambda string: {int(x) for x in string.split(',')} if string else None
    )

    DeclarativeActionContext.register_parser(
        'str_or_none',
        lambda string: string if string else None
    )

    DeclarativeActionContext.register_parser(
        'str_in_list',
        lambda string: [string] if isinstance(string, basestring) else None
    )

    # список строк через ',' (передается из окна выбора)
    DeclarativeActionContext.register_parser(
        'str_list',
        lambda string: string.split(',')
    )

    # json либо None
    DeclarativeActionContext.register_parser(
        'json_or_none',
        lambda string: json.loads(string) if string else None
    )
