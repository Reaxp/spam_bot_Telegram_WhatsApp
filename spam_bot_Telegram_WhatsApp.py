import time, pyautogui, keyboard

time.sleep(5)
f = open('text_spammer.txt', 'r')

for line in f:
    if not keyboard.is_pressed('space'):
        pyautogui.typewrite(line)
        pyautogui.press('enter')
    else:
        break
