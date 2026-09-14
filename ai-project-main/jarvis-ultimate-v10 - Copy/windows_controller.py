import pyautogui
import time
import subprocess

class WindowsController:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5

    def open_application(self, app_name):
        try:
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write(app_name, interval=0.05)
            time.sleep(0.5)
            pyautogui.press('enter')
            return f"Successfully executed launch sequence for {app_name}."
        except Exception as e:
            return f"System error launching {app_name}: {e}"

    def type_text(self, text):
        pyautogui.write(text, interval=0.02)
        return "Keyboard input completed."

    def execute_shortcut(self, *keys):
        pyautogui.hotkey(*keys)
        return f"Shortcut {'+'.join(keys)} executed."