# CV Service Architecture

## Purpose

The **CV (Computer Vision) service** is a long‑running microservice responsible for transforming raw visual input (frames) into **symbolic observations** that can be consumed by higher‑level components (e.g. the Governor or LLM services).

It is explicitly **not** responsible for:

* control or decision‑making
* language or reasoning
* training models
* system‑wide orchestration

Its single responsibility is **perception**.

---

## High‑level Responsibilities

The CV service:

* acquires visual frames from a configurable source
* interprets those frames into higher‑level representations
* runs continuously as a background perception loop
* exposes health and state endpoints for observability

---

## Container Boundary

The CV service runs in its own Docker container. This boundary exists because:

* CV has heavy, specialized dependencies (OpenCV, NumPy, possibly Torch later)
* CV may require hardware access (camera, GPU)
* CV evolves independently from control and language services

---

## Process Structure

Inside the container, there is a single Python process that hosts:

* a FastAPI application (for lifecycle & observability)
* a background perception loop (for frame processing)

FastAPI is the *entrypoint*; the perception loop is a *background task*.

---

## FastAPI Application (`app.py`)

The FastAPI app provides:

* `/health` — liveness and uptime information
* `/state` — current CV state summary (placeholder for future signal reporting)

FastAPI also owns the **application lifecycle**, which allows the perception loop to be started and stopped cleanly.

This design ensures the CV service is:

* inspectable
* monitorable
* controllable

---

## Perception Loop

Conceptually, the CV service runs the following loop:

```
frame → interpret → observation
```

This loop:

* runs continuously
* may be slowed or gated
* may later respond to attention or control signals

The loop itself is intentionally simple; complexity is pushed into modular components.

---

## Frame Acquisition Abstraction

### `FrameSource` (interface)

```python
class FrameSource(ABC):
    @abstractmethod
    def get(self) -> np.ndarray:
        ...
```

`FrameSource` defines a **contract** for anything that can produce frames.

This abstraction decouples:

* *where frames come from*
* from *how frames are interpreted*

The CV pipeline depends only on this interface, not on any specific capture technology.

---

## Concrete Frame Source Implementations

### `OpenCVFrameSource`

`OpenCVFrameSource` is a concrete implementation of `FrameSource` that:

* uses OpenCV
* opens a local camera device
* returns frames as NumPy arrays

OpenCV is fully isolated inside this adapter.

Future frame sources (e.g. screen capture, video playback, remote streams, test stubs) can be added without changing the rest of the CV system.

---

## Vision Interpretation

The **Vision Interpreter** consumes raw frames and produces symbolic observations.

Key properties:

* does not know where frames came from
* does not manage hardware or capture
* focuses purely on perception logic

This keeps interpretation testable and model‑agnostic.

---

## Composition Root (`worker.py`)

The composition root is where concrete implementations are wired together:

* choose a `FrameSource`
* instantiate the `VisionInterpreter`
* run the perception loop

This keeps configuration and wiring separate from core logic.

---

## Python Package Structure

```
cv/
├── app.py
├── worker.py
├── frame_sources/
│   ├── __init__.py
│   ├── base.py
│   └── opencv_source.py
├── vision/
│   └── interpreter.py
```

This structure enforces:

* explicit namespaces
* modular growth
* clean imports

---

## Architectural Principles

The CV service follows these principles:

* **Single Responsibility** — perception only
* **Dependency Inversion** — depend on interfaces, not implementations
* **Isolation of Messy Dependencies** — OpenCV stays behind adapters
* **Replaceability** — frame sources and interpreters are swappable
* **Observability First** — health and state are always available

---

## Future Extensions (No Refactor Required)

This architecture supports future work such as:

* attention‑gated perception
* multiple frame sources
* replay and debugging feeds
* GPU acceleration
* dynamic configuration
* richer state reporting

All without breaking existing contracts.

---

## Summary

The CV service is a microservice that runs a continuous perception loop, consuming frames through a pluggable interface and producing symbolic observations, with hardware and libraries cleanly isolated behind adapters.
