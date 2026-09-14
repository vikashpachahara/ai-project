import customtkinter as ctk
import threading

class JarvisUI:
    def __init__(self, core_system):
        self.core = core_system # Connects the UI to jarvis_main.py
        
        # Configure modern appearance
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        
        self.app = ctk.CTk()
        self.app.title("JARVIS Ultimate v10")
        self.app.geometry("600x500")
        
        self.setup_ui()

    def setup_ui(self):
        # Chat Display
        self.chat_box = ctk.CTkTextbox(self.app, width=560, height=350, state="disabled")
        self.chat_box.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
        
        # Input Field
        self.input_entry = ctk.CTkEntry(self.app, width=450, placeholder_text="Type a command...")
        self.input_entry.grid(row=1, column=0, padx=(20, 10), pady=10)
        self.input_entry.bind("<Return>", self.send_command)
        
        # Send Button
        self.send_button = ctk.CTkButton(self.app, width=100, text="Send", command=self.send_command)
        self.send_button.grid(row=1, column=1, padx=(0, 20), pady=10)

    def log_message(self, sender, text):
        """Updates the text box safely."""
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", f"{sender}: {text}\n\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")

    def send_command(self, event=None):
        command = self.input_entry.get()
        if not command:
            return
            
        self.input_entry.delete(0, 'end')
        self.log_message("You", command)
        
        # Send the command to JARVIS on a background thread so the UI doesn't freeze
        threading.Thread(target=self.process_command_thread, args=(command,), daemon=True).start()

    def process_command_thread(self, command):
        """Runs the LLM logic in the background."""
        response = self.core.brain.process_prompt(command)
        self.log_message("JARVIS", response)
        self.core.voice.speak(response)

    def run(self):
        self.log_message("System", "JARVIS UI initialized. Awaiting commands.")
        self.app.mainloop()