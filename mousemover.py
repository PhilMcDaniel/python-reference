import pyautogui
import random

#https://pyautogui.readthedocs.io/en/latest/

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(f"{screenWidth} by {screenHeight}")
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(f"The current mouse location is {currentMouseX}, {currentMouseY}")

#pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
print(screenWidth*-1)
print(screenHeight*-1)

x_delta = random.randint(currentMouseX*-1,(screenWidth - currentMouseX))
y_delta = random.randint(currentMouseY*-1,(screenHeight - currentMouseY))
print(f"Move the mouse {x_delta} pixels in the x-direction, and {y_delta} pixels in the y-direction")
pyautogui.move(x_delta,y_delta,.25)
pyautogui.click()
