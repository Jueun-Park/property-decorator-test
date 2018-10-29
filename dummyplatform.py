import time


class Platform(object):
    def __init__(self, data):
        self.data = data

    def _main(self):
        while True:
            time.sleep(2)
            steer, speed = self.data.control_data
            print("PLATFORM: !!!!! steer: {}, speed: {} !!!!!".format(steer, speed))
