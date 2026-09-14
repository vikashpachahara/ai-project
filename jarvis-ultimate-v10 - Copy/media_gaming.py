import pyautogui
import subprocess
import os

class MediaGaming:
    def __init__(self):
        # Default path for Epic Games on Windows
        self.epic_games_path = r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"

    def play_pause_media(self):
        pyautogui.press('playpause')
        return "Media toggled."

    def adjust_volume(self, direction="up", clicks=5):
        key = 'volumeup' if direction == "up" else 'volumedown'
        for _ in range(clicks):
            pyautogui.press(key)
        return f"Volume turned {direction}."

    def mute_audio(self):
        pyautogui.press('volumemute')
        return "Audio muted."

    def launch_epic_games(self):
        try:
            if os.path.exists(self.epic_games_path):
                subprocess.Popen(self.epic_games_path)
                return "Launching Epic Games Store."
            else:
                # Fallback to Windows search if path is different
                pyautogui.press('win')
                pyautogui.write('Epic Games', interval=0.05)
                pyautogui.press('enter')
                return "Searching for Epic Games."
        except Exception as e:
            return f"Failed to launch games: {str(e)}"