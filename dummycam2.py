import time


class DummyCam2(object):
    def __init__(self, data):
        self.data = data

    def _main(self):
        self.data.cam2data = 3
        while True:
            time.sleep(5)
            print("> cam1 data from cam2?: ", self.data.cam1data)
