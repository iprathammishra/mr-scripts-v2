import random
import os
import pyautogui
from time import sleep
rString = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCBNM1234567890'


def mloop(num) -> None:
    for _ in range(num):
        sleep(3)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.typewrite(
            "".join(list(random.sample(list(rString), random.randrange(5, 10)))))
        pyautogui.press('enter')


def main() -> None:
    actionDesk = int(input("Desktop Grind: "))
    actionMob = int(input("Mobile Grind: "))
    os.startfile('msedge')
    mloop(actionDesk)
    pyautogui.hotkey('ctrl', 'shift', 'i')
    sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'm')
    pyautogui.press('f5')
    sleep(2)
    mloop(actionMob)
    pyautogui.hotkey('ctrl', 'shift', 'm')
    pyautogui.hotkey('ctrl', 'shift', 'i')
    pyautogui.press('f5')


if __name__ == "__main__":
    main()
