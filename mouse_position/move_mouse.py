import pyautogui
import keyboard

print("start")
distance = 200
pyautogui.moveTo(300, 300)
while distance > 0:
    if keyboard.is_pressed('esc'): break
    pyautogui.move(distance, 0, duration=0.5)   # move right
    distance -= 20
    if keyboard.is_pressed('esc'): break
    pyautogui.move(0, distance, duration=0.5)   # move down
    if keyboard.is_pressed('esc'): break
    pyautogui.move(-distance, 0, duration=0.5)  # move left
    distance -= 20
    if keyboard.is_pressed('esc'): break
    pyautogui.move(0, -distance, duration=0.5)  # move up
    if distance == 0 :
        distance = 200
        pyautogui.moveTo(300, 300)