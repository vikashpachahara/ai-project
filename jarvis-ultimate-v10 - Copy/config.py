import os

class Config:
    # API Keys
    # We pull from environment variables to keep keys secure. 
    # (Set this in Windows: setx GEMINI_API_KEY "your_key_here")
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "enter your api")
    
    # Model Settings
    # Utilizing gemini-2.0-flash as the core brain for rapid multimodal reasoning
    PRIMARY_MODEL = "gemini-2.0-flash"
    MAX_OUTPUT_TOKENS = 2048
    TEMPERATURE = 0.7
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CACHE_DIR = os.path.join(BASE_DIR, "vision_cache")
    MEMORY_DB_PATH = os.path.join(BASE_DIR, "jarvis_memory.json")
    
    # System Prompt 
    # This dictates how JARVIS behaves globally
    SYSTEM_INSTRUCTION = (
        "You are JARVIS, an autonomous personal desktop AI assistant. "
        "You control a Windows environment. Be concise, highly capable, and "
        "prioritize direct answers without unnecessary formatting."
    )

    @classmethod
    def setup_directories(cls):
        if not os.path.exists(cls.CACHE_DIR):
            os.makedirs(cls.CACHE_DIR)