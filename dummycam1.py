import time


class DummyCam1(object):
    def __init__(self, data):
        self.data = data

    def _main(self):
        i = 0
        while True:
            time.sleep(1)
            self.data.cam1data = i
            print("CAM1: ", i)
            i += 1


if __name__ == "__main__":
    from dummydata import DummyData

    data = DummyData()
    dc1 = DummyCam1(data)
    dc1._main()
