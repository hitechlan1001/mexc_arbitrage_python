import pyautogui
import time
import keyboard
from datetime import datetime
import random

class WindowSwitcher:
    def __init__(self):
        self.is_running = False
        self.switch_interval = 2
        self.last_switch_time = None
        self.start_time = None
        self.screen_width, self.screen_height = pyautogui.size()
        self.scroll_amount = random.randint(500, 2000)
        # Disable fail-safe to prevent corner detection
        pyautogui.FAILSAFE = False
        
    def move_mouse_randomly(self):
        # Keep mouse away from screen edges to prevent fail-safe
        x = random.randint(100, self.screen_width - 100)
        y = random.randint(100, self.screen_height - 100)
        pyautogui.moveTo(x, y, duration=0.1)
        
    def perform_scroll(self):
        scroll_direction = random.choice([-1, 1])
        pyautogui.scroll(scroll_direction * self.scroll_amount)
        
    def start(self):
        self.is_running = True
        self.start_time = datetime.now()
        print("wallet tracking started. Press 'q' to quit.")
        self.last_switch_time = datetime.now()
        
        while self.is_running:
            current_time = datetime.now()
            time_diff = (current_time - self.last_switch_time).total_seconds()
            runtime = (current_time - self.start_time).total_seconds()
            
            if runtime >= 3600:  # 30 minutes = 1800 seconds
                self.is_running = False
                print("stop.")
                break
            
            if time_diff >= self.switch_interval:
                pyautogui.hotkey('alt', 'tab')
                self.move_mouse_randomly()
                
                self.perform_scroll()
                time.sleep(16)
                self.perform_scroll()
                time.sleep(17)
                self.perform_scroll()
                time.sleep(18)
                self.perform_scroll()
                time.sleep(19)
                
                self.last_switch_time = current_time
            
            if keyboard.is_pressed('q'):
                self.is_running = False
                print("Window switcher stopped.")
                break
                
            time.sleep(10)

if __name__ == "__main__":
    switcher = WindowSwitcher()
    switcher.start()
