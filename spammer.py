import pyautogui, time
time.sleep(3)
f = open("bee.txt", 'r')
counter = 0
for word in f:
  pyautogui.typewrite(word)
  pyautogui.press("enter")