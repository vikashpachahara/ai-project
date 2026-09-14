import psutil
import customtkinter as ctk
import threading

class StatusUI:
    def __init__(self):
        self.window = None

    def _build_window(self):
        self.window = ctk.CTk()
        self.window.title("JARVIS Vitals")
        self.window.geometry("250x120")
        
        # Keeps the vitals widget floating above other windows
        self.window.attributes("-topmost", True) 
        
        self.cpu_label = ctk.CTkLabel(self.window, text="CPU: 0%", font=("Consolas", 16, "bold"))
        self.cpu_label.pack(pady=(15, 5))
        
        self.ram_label = ctk.CTkLabel(self.window, text="RAM: 0%", font=("Consolas", 16, "bold"))
        self.ram_label.pack(pady=5)
        
        self.update_stats()
        self.window.mainloop()

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        
        self.cpu_label.configure(text=f"CPU Usage: {cpu}%")
        self.ram_label.configure(text=f"RAM Usage: {ram}%")
        
        # Color code warnings if usage is too high
        text_color = "red" if cpu > 85 or ram > 85 else "white"
        self.cpu_label.configure(text_color=text_color)
        self.ram_label.configure(text_color=text_color)
        
        # Refresh the data every 1.5 seconds
        self.window.after(1500, self.update_stats)

    def launch(self):
        """Runs the vitals window in a separate thread."""
        threading.Thread(target=self._build_window, daemon=True).start()
        return "System vitals overlay launched."