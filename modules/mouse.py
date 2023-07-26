import pyautogui
import random


SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

BUFFER_SIZE = 10

MoD = 0.1

def Z50_000_000_trotilla(NETROTILL):

    while NETROTILL > 0:

        ran_xp = random.randint(BUFFER_SIZE, SCREEN_WIDTH - BUFFER_SIZE)
        ran_yp = random.randint(BUFFER_SIZE, SCREEN_HEIGHT - BUFFER_SIZE)

        pyautogui.moveTo(ran_xp, ran_yp, duration = MoD)

        NETROTILL = NETROTILL - 1