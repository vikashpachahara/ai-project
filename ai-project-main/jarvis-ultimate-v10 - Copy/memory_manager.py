import json
import os
from config import Config

class MemoryManager:
    def __init__(self):
        self.db_path = Config.MEMORY_DB_PATH
        self.memory = self._load_memory()
        
    def _load_memory(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r') as f:
                    return json.load(f)
            except Exception:
                return {"facts": {}, "conversation_history": []}
        return {"facts": {}, "conversation_history": []}

    def _save_memory(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def learn_fact(self, key, value):
        """Saves a long-term preference or fact (e.g., learn_fact('name', 'Vikash'))"""
        self.memory["facts"][key] = value
        self._save_memory()
        return f"I will remember that {key} is {value}."

    def get_fact(self, key):
        return self.memory["facts"].get(key, None)

    def add_to_history(self, role, text):
        """Maintains a rolling buffer of the last 10 messages."""
        self.memory["conversation_history"].append({"role": role, "text": text})
        
        # Keep it lightweight to save tokens
        if len(self.memory["conversation_history"]) > 10:
            self.memory["conversation_history"].pop(0)
            
        self._save_memory()

    def get_context_string(self):
        """Compiles facts and history to inject into the LLM prompt."""
        context = "KNOWN FACTS:\n"
        for k, v in self.memory["facts"].items():
            context += f"- {k}: {v}\n"
            
        context += "\nRECENT CONVERSATION:\n"
        for msg in self.memory["conversation_history"]:
            context += f"{msg['role']}: {msg['text']}\n"
            
        return context