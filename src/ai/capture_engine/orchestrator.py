# orchestrator.py - simple loop that grabs frames and saves them when conditions met
import time, os, cv2
from .camera_manager import open_camera, read_frame
from .face_orientation import get_face_orientation
# expression detector placeholder uses cv2; import here to avoid circular
try:
    from .expression_detector import detect_expression
except Exception:
    def detect_expression(frame):
        return "neutral", 0.8

OUT_DIR = os.path.abspath(os.path.join(os.getcwd(),"..","..","data","captures"))
os.makedirs(OUT_DIR, exist_ok=True)

def save_frame(frame, name):
    path = os.path.join(OUT_DIR, name)
    cv2.imwrite(path, frame)
    print("SAVED", path)

def run_loop():
    print("Starting orchestrator... trying to open camera 0")
    try:
        cam = open_camera(0)
    except Exception as e:
        print("Camera open error:", e)
        return
    collected = set()
    start = time.time()
    while len(collected) < 6 and time.time() - start < 300:
        frame = read_frame(cam)
        if frame is None:
            continue
        yaw,pitch,roll = get_face_orientation(frame)
        expr,conf = detect_expression(frame)
        if expr == "neutral" and "frontal_neutra" not in collected:
            save_frame(frame, "frontal_neutra.jpg"); collected.add("frontal_neutra")
        if expr == "happy" and "sorriso" not in collected:
            save_frame(frame, "sorriso.jpg"); collected.add("sorriso")
        # simple sleep
        time.sleep(0.5)
    cam.release()
    print("Orchestrator finished. Collected:", collected)

if __name__ == '__main__':
    run_loop()
