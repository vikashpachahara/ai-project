import cv2
import threading

class CameraModule:
    def __init__(self):
        self.is_active = False
        self.camera_index = 0 # Default webcam

    def start_monitoring(self):
        if self.is_active:
            return "Camera is already monitoring."
        
        self.is_active = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()
        return "Background camera monitoring activated."

    def stop_monitoring(self):
        self.is_active = False
        return "Camera monitoring disabled."

    def _monitor_loop(self):
        cap = cv2.VideoCapture(self.camera_index)
        while self.is_active:
            ret, frame = cap.read()
            if not ret:
                print("[Camera] Frame capture failed.")
                break
            
            # Future expansion: Add OpenCV motion detection or face recognition here
            # cv2.imshow("JARVIS Background Feed", frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
                
        cap.release()
        cv2.destroyAllWindows()