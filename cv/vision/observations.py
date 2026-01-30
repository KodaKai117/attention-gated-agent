from dataclasses import dataclass
from typing import Dict, List


@dataclass
class VisualObservation: 
    timestamp: float
    labels: List[str]
    confidence: Dict[str, float]
    location: Dict[float, float]
