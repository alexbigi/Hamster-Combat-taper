import random
import time

import keyboard
import pyautogui


def check_button_position():
    while True:
        print(pyautogui.position())
        time.sleep(0.5)


def clicker():
    pyautogui.FAILSAFE = True
    while True:  # Start loop
        print(pyautogui.position())
        random_y = random.randint(744, 764)
        random_x = random.randint(1450, 1550)
        pyautogui.click(random_x, random_y)
        if keyboard.is_pressed("ctrl+c"):
            print("ctrl+c pressed")
            break


if __name__ == "__main__":
    # first where get coordinates of button
    # check_button_position()
    clicker()
