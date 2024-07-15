from pynput import keyboard
import pyautogui

def on_press(key):
    if key == keyboard.KeyCode(char='p'):
        currentMouseX, currentMouseY = pyautogui.position()
        print(f"Posição do mouse: ({currentMouseX}, {currentMouseY})")
        
listener = keyboard.Listener(on_press=on_press)

listener.start()
listener.join()
