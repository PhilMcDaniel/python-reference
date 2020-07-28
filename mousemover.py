import pyautogui
import random

#https://pyautogui.readthedocs.io/en/latest/

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
#print(f"{screenWidth} by {screenHeight}")
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#print(f"The current mouse location is {currentMouseX}, {currentMouseY}")

#pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
x_delta = random.randint(-500,500)
y_delta = random.randint(-500,500)
print(f"Move the mouse {x_delta} pixels in the x-direction, and {y_delta} pixels in the y-direction")
pyautogui.move(x_delta,y_delta,5)
pyautogui.click()
