from abc import ABC, abstractmethod
from typing import List, Dict
import numpy as np

class Detector(ABC):
    @abstractmethod
    def detect(self, frame: np.ndarray) -> List[Dict]:
        """
        Return structured detections from a frame.
        """
        pass
