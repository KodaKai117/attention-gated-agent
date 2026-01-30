# **Attention-Gated Agent – System Overview (v1)**

## **1\. Purpose**

This document provides a high-level overview of the Attention-Gated Agent system. It describes the system’s goals, core architectural principles, primary components, and interaction model. The intent is to establish a shared mental model for development, review, and iteration, rather than to specify implementation details.

This document is intentionally concise and focused on *what the system is* and *why it is structured this way*.

---

## **2\. System Summary**

The Attention-Gated Agent is a governed cognitive system that uses a Large Language Model (LLM) as a subordinate reasoning engine rather than as a direct interface or autonomous controller.

All external inputs (user interaction and environmental signals) are mediated by a central Governor component. The Governor explicitly controls attention allocation by deciding:

* Which inputs are observed  
* When perceptual subsystems are activated  
* What contextual information is passed to the LLM  
* When LLM inference is invoked

The system prioritizes explicit control, predictability, and extensibility over emergent autonomous behavior.

---

## **3\. Architectural Principles**

### **3.1 Explicit Attention Control**

Attention is implemented as an explicit control mechanism, not as an emergent property of the LLM. The system determines *what information exists for cognition* before reasoning occurs.

### **3.2 Mediated Interaction Model**

The LLM does not directly observe raw user input, screen data, or perceptual streams. All inputs are filtered, summarized, or suppressed by the Governor prior to inference.

### **3.3 Separation of Control and Cognition**

The system separates:

* **Control decisions** (what to attend to, when to reason)  
* **Cognitive processing** (semantic reasoning and synthesis)

This separation allows each layer to evolve independently.

### **3.4 Conservative MVP Scope**

Version 1 prioritizes deterministic behavior, debuggability, and cost control. Learning-based attention, long-term memory, and self-modifying behavior are explicitly out of scope.

## **4\. High-Level Components**

### **4.1 Governor**

The Governor is the central control component responsible for attention gating and system orchestration.

Responsibilities:

* Ingest and filter all external inputs  
* Control activation of perceptual subsystems (e.g., computer vision)  
* Construct and maintain the active working context  
* Decide when LLM inference is required  
* Mediate all outputs back to the user

The Governor performs no semantic reasoning beyond lightweight classification and routing.

---

### **4.2 LLM (Cognitive Core)**

The LLM functions as a non-interactive reasoning engine.

Responsibilities:

* Perform semantic reasoning and synthesis over curated context  
* Generate structured or textual outputs as requested by the Governor

Non-responsibilities:

* Direct user interaction  
* Attention allocation  
* Perceptual processing  
* Autonomous action selection

The LLM is invoked only when explicitly requested by the Governor.

---

### **4.3 Computer Vision (CV)**

The CV subsystem provides task-scoped visual perception over screen capture data.

Responsibilities:

* Extract symbolic or structured representations from screen frames  
* Operate at variable sampling rates as directed by the Governor

The CV subsystem does not interpret intent, maintain context, or communicate directly with the LLM.

---

### **4.4 User Interaction & Environment**

User chat input and screen capture are treated as external signals. These inputs are never directly exposed to the LLM and are subject to gating, filtering, and prioritization by the Governor.

---

## **5\. Interaction Model (High Level)**

1. External input is received (user message, screen update, or both)  
2. The Governor evaluates relevance and system state  
3. The Governor enables or suppresses perceptual subsystems as needed  
4. The Governor constructs an active working context  
5. The LLM is optionally invoked with this context  
6. The Governor mediates and returns the final response

At any point, the Governor may decide that no LLM invocation is necessary.

---

## **7\. Evolution Path (Informal)**

Future versions may introduce:

* Learned prioritization signals to assist the Governor  
* Episodic or task-scoped memory  
* More granular attention budgets  
* Additional perceptual or symbolic subsystems

These extensions are intended to build on the existing control-first architecture rather than replace it.

---

## **8\. Design Rationale (Summary)**

This architecture favors explicit control and clarity over maximum autonomy. By subordinating cognition to governance, the system remains predictable, inspectable, and suitable for incremental evolution.

The core hypothesis is that attention, when treated as a system-level concern rather than a model-internal artifact, enables more robust and efficient agent behavior.

