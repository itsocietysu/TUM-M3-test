# coding: utf-8
from m3demo.core.controllers import main_controller

from .main.actions import Pack


def register_actions():
    main_controller.extend_packs((
        Pack(),
    ))
