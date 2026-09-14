import pyttsx3
import speech_recognition as sr

class VoiceEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id) 
        self.engine.setProperty('rate', 170) 

    def speak(self, text):
        print(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio)
                print(f"You: {command}")
                return command
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return "Speech recognition service offline."
            except Exception:
                return ""