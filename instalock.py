import time
import pyautogui
import keyboard
import configparser


def wait_for_keyboard_press():
    print("InstaLock Ready (L)")
    while True:
        if keyboard.is_pressed('l'):
            print("")
            time.sleep(0.2)
            break


while True:
    wait_for_keyboard_press()
    pyautogui.click(1000, 920)
    time.sleep(0.1)
    pyautogui.click(1000, 920)
    time.sleep(0.1)
    pyautogui.click(1000, 800)
    time.sleep(0.1)
    pyautogui.click(600, 800)
    time.sleep(0.1)
    pyautogui.click(999, 800)
    time.sleep(0.1)
    pyautogui.click()
