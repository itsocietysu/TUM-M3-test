# coding: utf-8
from objectpack.ui import ModelEditWindow

from m3demo.core.utils.misc import ModelRegister
from m3demo.core.utils.ui import reorder_controls
from m3demo.core.controllers import core_observer

from ..models import Candidate


class EditWindow(ModelEditWindow):

    model = Candidate

    _field_list = (
        'name',
        'planet_id',
        'age',
        'email'
    )
    field_fabric_params = dict(
        field_list=_field_list,
        model_register=ModelRegister({
            'Planet': __package__ + '.actions.PlanetsPack',
        }, core_observer),
    )

    def _do_layout(self):
        reorder_controls(self._controls, self._field_list)

        super(EditWindow, self)._do_layout()
