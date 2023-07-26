import pyautogui
import random

pyautogui.FAILSAFE = True

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

BUFFER_SIZE = 10

MoD = 0.1
if __name__ == "__main__":

    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

    while True:

        ran_xp = random.randint(BUFFER_SIZE, SCREEN_WIDTH - BUFFER_SIZE)
        ran_yp = random.randint(BUFFER_SIZE, SCREEN_HEIGHT - BUFFER_SIZE)

        pyautogui.moveTo(ran_xp, ran_yp, duration = MoD)