import pyautogui
import time
import pyperclip


pyautogui.click(925,740)
time.sleep(1)

pyautogui.moveTo(488,167)
pyautogui.dragTo(1313,634, duration=1.0, button="left")

pyautogui.hotkey('ctrl','c')
pyautogui.click(1313,634)
time.sleep(1)

text = pyperclip.paste()
print(text)

pyautogui.click(1252,16)





