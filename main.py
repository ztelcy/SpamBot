# Automated text messaging

# Import relevant modules
import time
import pyautogui

# Let's do some coding!
def SendMessage():
    time.sleep(8)
    text = open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendMessage()
