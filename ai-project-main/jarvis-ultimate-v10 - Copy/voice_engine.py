import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import os

class VoiceEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.sample_rate = 44100  
        self.record_seconds = 5  
        
        # Setup AI Voice
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id) 
        self.engine.setProperty('rate', 170) 

    def speak(self, text):
        print(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        print("\n[Microphone Active] Listening for 5 seconds...")
        temp_file = "jarvis_temp_voice.wav"
        
        try:
            # 1. Capture audio via sounddevice instead of pyaudio
            recording = sd.rec(int(self.record_seconds * self.sample_rate), 
                               samplerate=self.sample_rate, 
                               channels=1, 
                               dtype='int16')
            sd.wait()  
            
            # 2. Save it temporarily
            write(temp_file, self.sample_rate, recording)
            
            # 3. Read and translate the voice file
            with sr.AudioFile(temp_file) as source:
                audio_data = self.recognizer.record(source)
                command = self.recognizer.recognize_google(audio_data)
                print(f"You: {command}")
                
            # Clean up the temp file
            if os.path.exists(temp_file):
                os.remove(temp_file)
                
            return command
            
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"[Voice Error]: {e}")
            return ""