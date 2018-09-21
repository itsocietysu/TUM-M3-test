# coding: utf-8
from objectpack.ui import ModelEditWindow

from m3demo.core.utils.ui import reorder_controls

from ..models import Test


class EditWindow(ModelEditWindow):

    model = Test

    _field_list = (
        'test',
    )
    field_fabric_params = dict(
        field_list=_field_list,
    )

    def _do_layout(self):
        reorder_controls(self._controls, self._field_list)

        super(EditWindow, self)._do_layout()
