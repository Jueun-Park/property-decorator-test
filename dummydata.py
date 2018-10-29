class DummyData(object):
    def __init__(self):
        self._cam1data: int = None
        self._cam2data: int = None
        self._control_steer = None
        self._control_speed = None

    @property
    def cam1data(self):
        return self._cam1data

    @cam1data.setter
    def cam1data(self, value: int):
        self._cam1data = value

    @property
    def cam2data(self):
        return self._cam2data

    @cam2data.setter
    def cam2data(self, value):
        self._cam2data = value

    @property
    def control_data(self):
        return self._control_steer, self._control_speed

    @control_data.setter
    def control_data(self, control_list: list):
        self._control_steer = control_list[0]
        self._control_speed = control_list[1]
