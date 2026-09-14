from flask import Flask, request, jsonify
import threading
import socket

class PhoneConnector:
    def __init__(self, core_system):
        self.core = core_system
        self.app = Flask(__name__)
        self.port = 5000
        self.setup_routes()

    def get_local_ip(self):
        """Finds your PC's local IP address so you can connect from your phone."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"

    def setup_routes(self):
        @self.app.route('/send_command', methods=['POST'])
        def receive_command():
            data = request.json
            command = data.get('command', '')
            
            if command:
                print(f"\n[Phone] Received: {command}")
                # Pass the phone's command to the AI brain
                response = self.core.brain.process_prompt(command)
                self.core.voice.speak(response)
                
                # If the UI is active, log it there too
                if hasattr(self.core, 'ui'):
                    self.core.ui.log_message("Poco X7 Pro", command)
                    self.core.ui.log_message("JARVIS", response)
                    
                return jsonify({"status": "success", "response": response})
            return jsonify({"status": "error", "message": "No command provided"}), 400

    def start_server(self):
        """Runs the listener server in the background."""
        ip = self.get_local_ip()
        print(f"Phone Connector active. Send POST requests to http://{ip}:{self.port}/send_command")
        
        # Run Flask in a background thread so it doesn't freeze the main app
        server_thread = threading.Thread(
            target=lambda: self.app.run(host='0.0.0.0', port=self.port, debug=False, use_reloader=False),
            daemon=True
        )
        server_thread.start()