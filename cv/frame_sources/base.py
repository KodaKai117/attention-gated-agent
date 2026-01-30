from abc import ABC, abstractmethod
import numpy as np


class FrameSource(ABC):
    @abstractmethod
    def get(self) -> np.ndarray:
        """
        Return a single frame as a numpy array.
        May block until a frame is available.
        """
        pass
