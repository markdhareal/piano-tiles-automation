import pyautogui
import keyboard
import time
import win32api, win32con

# COORDINATES
# Tile 1: Point(x=435, y=564)
# Tile 2: Point(x=564, y=564)
# Tile 3: Point(x=690, y=564)
# Tile 4: Point(x=817, y=564)

# RGB COLORS
# Red: 0 Green: 0 Blue: 0

def left_click(x,y):
    win32api.SetCursorPos((x, y))
    # LEFT CLICK
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # DELAY
    time.sleep(0.01)
    # LEFT CLICK RELEASE
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)