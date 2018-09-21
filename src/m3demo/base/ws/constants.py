# coding: utf-8
u"""Константы, используемые при описании веб-сервисов."""


#: Атрибуты обязательного параметра веб-сервиса.
REQUIRED_PARAM_ATTRIBUTES = dict(
    nillable=False,
    min_occurs=1,
    max_occurs=1,
)

#: Атрибуты необязательного параметра веб-сервиса.
NON_REQUIRED_PARAM_ATTRIBUTES = dict(
    nillable=True,
    min_occurs=0,
    max_occurs=1,
)
