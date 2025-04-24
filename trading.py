import pyautogui
import time

# Pause between actions (feels more human)
# pyautogui.PAUSE = 0.2

# Delay to switch to MEXC tab after starting script
print("⏳ Switch to the MEXC UI within 5 seconds...")
time.sleep(3)
start_at = time.time() * 1000

pyautogui.click(x=1680, y=296)  # 👈 Replace with sell button position
# Step 1: Click 'Amount' input field (manually update coords)
pyautogui.doubleClick(x=1785, y=496)
 # 👈 Replace with real position
pyautogui.typewrite('0.01')     # Type amount

# Step 3: Click 'Sell SOL' button
pyautogui.click(x=1744, y=578)  # 👈 Replace with sell button position

end_at = time.time() * 1000
diff = end_at - start_at
print('speed',diff)
# Optional: Confirm sell (if confirmation popup appears)
time.sleep(1)
# pyautogui.press('enter')       # Confirms the dialog (if any)

print("✅ Sell order submitted (if all positions were correct).")




# Buy: x=1680, y=296
# Sell: x=1816, y=297
# Input: x=1785, y=496
# Confirm: x=1744, y=578
