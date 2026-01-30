import time
from frame_sources.opencv_source import OpenCVFrameSource
from vision.interpreter import VisionInterpreter
from detectors.dummy_detector import DummyDetector

def publish(observation):
    print(observation)


def run():
    source = OpenCVFrameSource(device=0)
    detector = DummyDetector()
    interpreter = VisionInterpreter()

    try:
        while True:
            frame = source.get()
            detections = detector.detect(frame)
            obs = interpreter.interpret(detections)#this should interpret the output of the object detection model in detectors; whereby frame is passed to the object detector
            publish(obs)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        source.release()
