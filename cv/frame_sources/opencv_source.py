import cv2
import numpy as np
from .base import FrameSource


class OpenCVFrameSource(FrameSource):
    def __init__(self, device: int = 0):
        self.cap = cv2.VideoCapture(device)
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open camera device {device}")

    def get(self) -> np.ndarray:
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to read frame from camera")
        return frame

    def release(self):
        self.cap.release()
