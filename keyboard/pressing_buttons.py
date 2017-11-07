import pyautogui

# Press specified button one time
pyautogui.press("enter")

# Press specified button several times
pyautogui.press("enter", presses=2)

# Press specified button several times, pausing for given number of seconds after each press
pyautogui.press("a", presses=3, interval=0.5)

# You can also use action keys
pyautogui.press("scrolllock")

# Press multiple keys, one after another
pyautogui.press(["a", "b", "c"])

# You can do it also several times with given interval
pyautogui.press(["a", "b", "c"], presses=3, interval=0.5)

# Hold down specified key
pyautogui.keyDown("shift")

pyautogui.press("a", presses=3)

# Stop holding specified key
pyautogui.keyUp("shift")

pyautogui.press("a", presses=3)

# Press and hold several keys in given order, and then release them in reverse order
# Useful for using shortcuts
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "alt", "delete")
