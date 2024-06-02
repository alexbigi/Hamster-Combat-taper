import logging
import random
import threading

from ppadb.client import Client as AdbClient


def init():
    logging.getLogger("ppadb").setLevel(logging.DEBUG)
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    if len(devices) > 0:
        device = devices[0]
        device.shell("input tap 727 1694")
        while True:
            random_y = random.randint(1300, 1700)
            random_x = random.randint(300, 777)
            device.shell(f"input tap {random_x} {random_y}")
    else:
        return


if __name__ == "__main__":
    thread_one = threading.Thread(target=init, daemon=True)
    thread_two = threading.Thread(target=init, daemon=True)
    thread_three = threading.Thread(target=init, daemon=True)
    thread_four = threading.Thread(target=init, daemon=True)
    thread_five = threading.Thread(target=init, daemon=True)
    thread_six = threading.Thread(target=init, daemon=True)
    thread_seven = threading.Thread(target=init, daemon=True)
    thread_eight = threading.Thread(target=init, daemon=True)
    thread_nine = threading.Thread(target=init, daemon=True)
    thread_one.start()
    thread_two.start()
    thread_three.start()
    thread_four.start()
    thread_five.start()
    thread_six.start()
    thread_seven.start()
    thread_eight.start()
    thread_nine.start()
    answer = input('Exit?\n')

