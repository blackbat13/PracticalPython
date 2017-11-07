import pyautogui

# Move mouse to specified position (x,y) on the screen
pyautogui.moveTo(x=1000, y=150)

# Move mouse to specified position telling how much time this should take
# Duration is given in seconds
pyautogui.moveTo(x=1000, y=500, duration=2.0)

# Change only y coordinate of the mouse. Leave x unchanged.
pyautogui.moveTo(x=None, y=600, duration=2.0)

# Change only x coordinate of the mouse. Leave y unchanged.
pyautogui.moveTo(x=800, y=None, duration=2.0)

# Move mouse by specified values
pyautogui.moveRel(xOffset=100, yOffset=-100, duration=2.0)

# Specify HOW mouse should move, i.e. the easing function.
# You can get fancy results with that.
# Experiment with different easing functions (they all begin with "ease").
pyautogui.moveTo(x=500, y=500, duration=2.0, tween=pyautogui.easeInBounce)

pyautogui.moveRel(xOffset=300, yOffset=100, duration=2.0, tween=pyautogui.easeInCirc)
