
import time
import pyautogui

def click_at_coordinates(x, y):
    # Wait for 10 seconds
    time.sleep(10)
    # Move the mouse to the specified coordinates and click
    pyautogui.click(x, y)

# Call the function with the desired coordinates
click_at_coordinates(226, 251)
