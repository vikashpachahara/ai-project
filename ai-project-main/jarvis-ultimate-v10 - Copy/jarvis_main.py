import threading
import time

# Core Intelligence & Memory
from config import Config
from llm_brain import JarvisBrain
from memory_manager import MemoryManager
from recovery_engine import RecoveryEngine

# Automation & OS Control
from windows_controller import WindowsController
from dev_agent import DevAgent
from media_gaming import MediaGaming

# Senses (Vision, Voice, Web)
from voice_engine import VoiceEngine
from vision_engine import VisionEngine
from camera_module import CameraModule
from internet_researcher import InternetResearcher
from browser_agent import BrowserAgent

# UI & Hardware
from app_ui import JarvisUI
from status_ui import StatusUI
from phone_connector import PhoneConnector

class JarvisCore:
    def __init__(self):
        print("Booting JARVIS Ultimate v10...")
        
        # 1. Initialize Voice first so JARVIS can speak during boot
        self.voice = VoiceEngine()
        self.voice.speak("Initializing core systems.")
        
        # 2. Initialize Brain & Memory
        self.memory = MemoryManager()
        self.brain = JarvisBrain()
        self.recovery = RecoveryEngine(self.voice)
        
        # 3. Initialize Agents & OS Controllers
        self.os = WindowsController()
        self.dev = DevAgent()
        self.media = MediaGaming()
        self.web = InternetResearcher()
        self.browser = BrowserAgent()
        
        # 4. Initialize Hardware/UI links
        self.camera = CameraModule()
        self.vitals = StatusUI()
        self.phone = PhoneConnector(self)
        
        self.is_running = True

    def start(self):
        self.voice.speak("All systems online. Launching interfaces.")
        
        # Launch phone server and system vitals overlay in the background
        self.phone.start_server()
        self.vitals.launch()
        
        # Start background listener (for continuous camera/voice monitoring)
        threading.Thread(target=self.background_listener, daemon=True).start()
        
        # Launch the main CustomTkinter UI dashboard (this replaces the terminal loop)
        self.ui = JarvisUI(self)
        self.ui.run()

    def background_listener(self):
        while self.is_running:
            # Future logic for hotword detection or motion sensing goes here
            time.sleep(1)

    def shutdown(self):
        self.voice.speak("Powering down all systems.")
        self.is_running = False
        self.browser.close_browser()
        self.camera.stop_monitoring()
        if hasattr(self, 'ui'):
            self.ui.app.quit()

if __name__ == "__main__":
    Config.setup_directories()
    jarvis = JarvisCore()
    jarvis.start()