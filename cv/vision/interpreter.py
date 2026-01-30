import time
import numpy as np
from typing import List, Dict
from .observations import VisualObservation



class VisionInterpreter:
    def __init__(self, cursor_pos=(0.5, 0.5)):
        #cursor_pos is normalized screen space
        self.cursor_x, self.cursor_y = cursor_pos

    def interpret(self, detections: List[Dict]) -> VisualObservation:
        # Placeholder logic — replace later with real vision, also need to get some metrics to look at the right Dict keys from detections
        timestamp = time.time()

        labels = []
        confidence = {}

        # Default values
        location = {"x": 0.0, "y": 0.0}
        distancefromcursor = float("inf")
        iscursor = False

        if detections:
            d = detections[0]  # dumb-for-now: first detection

            labels.append(d["label"])
            confidence[d["label"]] = d["confidence"]

            bbox = d["bbox"]
            cx = (bbox["x1"] + bbox["x2"]) / 2
            cy = (bbox["y1"] + bbox["y2"]) / 2

            # Assume bbox coords already normalized or normalize earlier
            location = {"x": cx, "y": cy}

            dx = cx - self.cursor_x
            dy = cy - self.cursor_y
            distancefromcursor = (dx**2 + dy**2) ** 0.5

            iscursor = d["label"] == "cursor"

        return VisualObservation(
            timestamp=timestamp,
            labels=labels,
            confidence=confidence,
            location=location,
            distancefromcursor=distancefromcursor,
            iscursor=iscursor
        )


#Idea is to refine the data to conform to the attributes defined in the
#dataclass. distancefromcursor is a proxy for importance - used to restrict the data that gets through to the llm in an effort to steer attention in real time.
