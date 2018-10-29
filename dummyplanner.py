import time


class Planner(object):
    def __init__(self, data):
        self.data = data

    def _main(self):
        while True:
            time.sleep(3)
            try:
                steer = self.data.cam1data * 2
                speed = self.data.cam2data * 3
                self.data.control_data = [steer, speed]
            except TypeError:
                pass
