import time
import numpy as np
from .observations import VisualObservation


class VisionInterpreter:
    def interpret(self, frame: np.ndarray) -> VisualObservation:
        # Placeholder logic — replace later with real vision
        return VisualObservation(
            timestamp=time.time(),
            labels=["unknown"],
            confidence={"unknown": 1.0},
        )
