import pyautogui

# Write a message on the keyboard
pyautogui.typewrite(message="Hello World!")

# Write a message on the keyboard pausing for given time after each character
# Interval is given in seconds
pyautogui.typewrite(message="Slow Hello World!", interval=0.2)
