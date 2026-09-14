import os
import logging
from PIL import ImageGrab
from google import genai
from google.genai import types
from config import GEMINI_API_KEY

class VisionEngine:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.vision_model = "gemini-2.5-flash"
        logging.info("Vision Engine Online.")

    def capture_screen(self, save_path="memory/current_screen.png") -> str:
        """Captures the current desktop screen."""
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        screenshot = ImageGrab.grab()
        screenshot.save(save_path)
        return save_path

    def analyze_screen(self, prompt: str) -> str:
        """Sends the screen to Gemini to understand the UI or verify actions."""
        img_path = self.capture_screen()
        logging.info(f"Analyzing screen for: {prompt}")
        
        try:
            from PIL import Image
            img = Image.open(img_path)
            
            response = self.client.models.generate_content(
                model=self.vision_model,
                contents=[
                    img,
                    types.Part.from_text(text=prompt)
                ]
            )
            return response.text
        except Exception as e:
            logging.error(f"Vision analysis failed: {e}")
            return f"Error analyzing screen: {str(e)}"