import pyautogui
import time

num = int(input("Enter your number: "))
time.sleep(2)
    
for i in range(1, num + 1):
    pyautogui.typewrite("#" * i)
    pyautogui.press("enter")
