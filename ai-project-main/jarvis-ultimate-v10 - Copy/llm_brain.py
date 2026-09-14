import os
from config import Config
from google import genai

class JarvisBrain:
    def __init__(self):
        # Assumes you have GEMINI_API_KEY set as an environment variable
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        self.chat_session = self.client.chats.create(model="gemini-3.6-flash")
        
    def process_prompt(self, user_input):
        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Error communicating with Gemini API: {str(e)}"

if __name__ == "__main__":
    brain = JarvisBrain()
    print("JARVIS Brain Online. Type 'exit' to quit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            break
        print(f"JARVIS: {brain.process_prompt(prompt)}")