import threading
from dummycam1 import DummyCam1
from dummycam2 import DummyCam2
from dummydata import DummyData
from dummyplanner import Planner
from dummyplatform import Platform


def main():
    """
    각 함수는 이미 while loop 를 가지고 있다.
    [인스턴스].[메인 메서드]()를 쓰레드로 만들어 실행시킨다.
    :return:
    """
    data = DummyData()

    dc1 = DummyCam1(data)
    dc2 = DummyCam2(data)
    planner = Planner(data)
    platform = Platform(data)

    t_dc1 = threading.Thread(target=dc1._main)
    t_dc2 = threading.Thread(target=dc2._main)
    t_p = threading.Thread(target=planner._main)
    t_pf = threading.Thread(target=platform._main)

    t_dc1.start()
    t_dc2.start()
    t_p.start()
    t_pf.start()


if __name__ == "__main__":
    main()
