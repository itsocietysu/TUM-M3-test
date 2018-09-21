# coding: utf-8
# pylint: disable=function-redefined
import locale

from django.apps import AppConfig


class AppConfig(AppConfig):

    name = __package__

    def _set_locale(self):
        u"""Настройка параметров локали."""
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    def _register_dac_parsers(self):
        u"""Регистрация дополнительных парсеров для параметров контекста."""
        from .dac import register_dac_parsers

        register_dac_parsers()

    def _init_educommon(self):
        u"""Настройка educommon."""
        from educommon import ioc
        from m3demo.core.controllers import core_observer
        from m3demo.core.controllers import main_controller

        ioc.register('observer', core_observer)
        ioc.register('main_controller', main_controller)

    def _patch_migration_writer(self):
        u"""Исправление метода MigrationWriter.serialize().

        Цель изменения - отображение в коде генерируемых миграций символов
        Unicode.
        """
        from django.db.migrations import writer

        class MigrationWriter(writer.MigrationWriter):

            @classmethod
            def serialize(cls, value):
                res, imps = super(MigrationWriter, cls).serialize(value)

                if isinstance(res, basestring) and '\\u' in res:
                    res = res.decode('unicode_escape')

                return res, imps

            def as_string(self):
                result = super(MigrationWriter, self).as_string()

                try:
                    import yapf
                except ImportError:
                    from django.core.exceptions import ImproperlyConfigured
                    raise ImproperlyConfigured(
                        'Please, install yapf (pip install yapf).'
                    )
                else:
                    result = yapf.yapf_api.FormatCode(
                        unformatted_source=result.decode('utf-8'),
                        style_config='pep8',
                        verify=True,
                    )[0].encode('utf-8')

                result = result.replace('# -*- coding: utf-8 -*-',
                                        '# coding: utf-8')

                return result

        writer.MigrationWriter = MigrationWriter

    def _init_m3_dev_utils(self):
        u"""Настройка пакета m3-dev-utils."""
        from django.conf import settings
        from educommon.utils.misc import cached_property
        import m3_dev_utils

        class Config(m3_dev_utils.Config):

            @cached_property
            def controller(self):
                from m3demo.core.controllers import main_controller
                return main_controller

            @cached_property
            def observer(self):
                from m3demo.core.controllers import core_observer
                return core_observer

        m3_dev_utils.config = Config()

    def ready(self):
        self._set_locale()
        self._register_dac_parsers()
        self._init_educommon()
        self._patch_migration_writer()
        self._init_m3_dev_utils()

        super(AppConfig, self).ready()
