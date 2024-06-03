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
        # device.shell("input tap 727 1694")
        while True:
            random_y = random.randint(1300, 1700)
            random_x = random.randint(300, 777)
            device.shell(f"monkey tap {random_x} {random_y}")
    else:
        return


if __name__ == "__main__":
    threading.Thread(target=init, daemon=True).start()
    answer = input('Exit?\n')
