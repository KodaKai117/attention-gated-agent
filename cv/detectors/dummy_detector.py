from typing import List, Dict
import numpy as np
from .base import Detector


class DummyDetector(Detector):
    """
    A placeholder detector that returns a single fake detection.
    Useful for wiring, testing, and development.
    """

    def detect(self, frame: np.ndarray) -> List[Dict]:
        height, width = frame.shape[:2]

        # Fake bounding box roughly centered
        bbox = {
            "x1": int(width * 0.4),
            "y1": int(height * 0.4),
            "x2": int(width * 0.6),
            "y2": int(height * 0.6),
        }

        return [
            {
                "label": "dummy_object",
                "confidence": 1.0,
                "bbox": bbox,
            }
        ]
