import subprocess
import os

class DevAgent:
    def __init__(self):
        self.workspace_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jarvis_workspace")
        if not os.path.exists(self.workspace_dir):
            os.makedirs(self.workspace_dir)

    def run_terminal_command(self, command):
        """Executes a shell command and returns the output."""
        try:
            # Using subprocess.run as it is the recommended approach for invoking subprocesses
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                cwd=self.workspace_dir
            )
            
            output = result.stdout if result.stdout else result.stderr
            
            if result.returncode == 0:
                return f"Command executed successfully:\n{output}"
            else:
                return f"Command failed (Exit code {result.returncode}):\n{output}"
                
        except Exception as e:
            return f"Error executing command: {str(e)}"

    def write_and_run_python(self, code_string, filename="temp_script.py"):
        """Writes Python code to a file and executes it."""
        filepath = os.path.join(self.workspace_dir, filename)
        
        try:
            with open(filepath, "w") as f:
                f.write(code_string)
            
            # Execute the newly created Python file
            return self.run_terminal_command(f"python {filename}")
            
        except Exception as e:
            return f"Failed to run code: {str(e)}"