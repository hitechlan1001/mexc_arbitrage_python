import pyautogui
import time

print("Move your mouse to the target position (5 sec)...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Mouse position: x={x}, y={y}")