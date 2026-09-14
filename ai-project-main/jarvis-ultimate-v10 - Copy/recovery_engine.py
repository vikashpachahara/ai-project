import traceback
import time

class RecoveryEngine:
    def __init__(self, voice_engine):
        self.voice = voice_engine
        self.error_log = "jarvis_crash_reports.txt"

    def execute_safely(self, func, *args, **kwargs):
        """Wraps any function execution in a safety net."""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_details = traceback.format_exc()
            self.log_error(str(e), error_details)
            
            warning = f"A system error occurred in the {func.__name__} module. Check the crash report."
            print(f"[RECOVERY ENGINE] {warning}")
            self.voice.speak("I encountered an error executing that command. Logging details.")
            return None

    def log_error(self, error_msg, trace):
        with open(self.error_log, "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] ERROR: {error_msg}\n")
            f.write(f"{trace}\n{'-'*40}\n")