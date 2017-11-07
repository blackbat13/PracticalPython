import pyautogui

# Show simple alert box
# You can modify text content, title and even the label on the button
pyautogui.alert(text="This is an alert!", title="Example alert", button="OK")

# Show simple confirm message box
# You can specify several buttons
# It returns answer specified by the user
answer = pyautogui.confirm(text='You should confirm that', title='Please confirm', buttons=['OK', 'Cancel', "OH NO!"])

print(f"That was your answer: {answer}")

# Ask user for input
answer = pyautogui.prompt(text="Please write something", title="Awaiting your input")
print(f"That was your answer: {answer}")

# We can also enter default answer for user
answer = pyautogui.prompt(text="How old are you?", title="Confirm your age", default="26")
print(f"That was your answer: {answer}")

# Ask user for password
password = pyautogui.password(text="Enter your password", title="Secret")
print(f"Your password is: {password}")

# Give user default password
password = pyautogui.password(text="Enter your password", title="Secret", default="admin123")
print(f"Your password is: {password}")

# Use different mask
password = pyautogui.password(text="Enter your password", title="Secret", mask="@")
print(f"Your password is: {password}")
