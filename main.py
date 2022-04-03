import pyautogui

position = pyautogui.position()
print(position)

pyautogui.moveTo(139, 290, duration=1)
pyautogui.move(100, 0, duration=1)

#Right-click on windows
pyautogui.click(139, 280, clicks=2)
pyautogui.click(139, 280, button='right')


#Documentation --> https://pyautogui.readthedocs.io/en/latest/