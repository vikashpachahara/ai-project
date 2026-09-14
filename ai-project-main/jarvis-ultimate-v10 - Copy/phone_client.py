import socket
import json
import subprocess
import os

# Set this to your PC's local IP address (find it by running 'ipconfig' in PC terminal)
PC_IP_ADDRESS = "192.168.1.100" 
PORT = 9999

def execute_phone_action(action, data):
    print(f"Executing: {action} with data: {data}")
    
    if action == "open_browser":
        # Android intent command
        os.system(f"am start -a android.intent.action.VIEW -d '{data}'")
    elif action == "toast":
        os.system(f"termux-toast '{data}'")
    elif action == "vibrate":
        os.system("termux-vibrate -d 500")
    elif action == "battery":
        os.system("termux-battery-status")

def connect_to_jarvis():
    while True:
        try:
            print(f"Connecting to JARVIS at {PC_IP_ADDRESS}:{PORT}...")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((PC_IP_ADDRESS, PORT))
            print("Connected to JARVIS PC!")
            
            while True:
                data = client.recv(1024)
                if not data:
                    break
                payload = json.loads(data.decode('utf-8'))
                execute_phone_action(payload.get("action"), payload.get("data", ""))
        except Exception as e:
            print(f"Connection lost. Retrying in 5 seconds... ({e})")
            import time
            time.sleep(5)

if __name__ == "__main__":
    connect_to_jarvis()