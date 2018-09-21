# coding: utf-8
from spyne.model.complex import ComplexModelBase
from spyne.model.complex import ComplexModelMeta


class ComplexModel(ComplexModelBase):

    u"""Базовый класс для типов данных, используемых в веб-сервисах.

    Дополняет :class:`spyne.model.complex.ComplexModelBase` указанием
    пространства имен ``http://bars-open.ru/inf``.
    """

    __metaclass__ = ComplexModelMeta
    __namespace__ = 'http://bars-open.ru/inf'
