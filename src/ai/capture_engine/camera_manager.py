# camera_manager.py - minimal camera helper
import cv2

def open_camera(idx=0):
    cam = cv2.VideoCapture(idx)
    if not cam.isOpened():
        raise RuntimeError("Camera not available")
    return cam

def read_frame(cam):
    ret, frame = cam.read()
    if not ret:
        return None
    return frame
