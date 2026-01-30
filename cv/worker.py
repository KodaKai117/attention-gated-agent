import time
from frame_sources.opencv_source import OpenCVFrameSource
from vision.interpreter import VisionInterpreter


def publish(observation):
    print(observation)


def run():
    source = OpenCVFrameSource(device=0)
    interpreter = VisionInterpreter()

    try:
        while True:
            frame = source.get()
            obs = interpreter.interpret(frame)
            publish(obs)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        source.release()
