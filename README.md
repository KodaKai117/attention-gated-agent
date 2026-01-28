# Attention-Gated Agent

This project explores an alternative agent architecture in which:
- perception
- cognition (LLMs)
- executive control

are explicitly separated and coordinated by a governing process that owns time, attention, and action.

## Core Principles

- **Silence by default**: the system prefers not to act
- **Attention is scarce**: cognition is invoked selectively
- **Human-like I/O**: interaction occurs via screen, keyboard, mouse, and audio
- **Governance over capability**: alignment is architectural, not prompt-based

## Architecture

The system is composed of three primary services:

- **CV** — perception only, no decision-making
- **LLM** — cognition on demand, no agency
- **Governor** — executive function and attention control

All services are containerized and communicate over explicit interfaces.

## Status

Early-stage MVP.  
Current focus: structural correctness, not performance.

## Non-Goals (for now)

- Autonomous goal pursuit
- Conversational agents
- Tool-using LLM demos

## Motivation

The hypothesis is that safer and more useful agents emerge not from more capable models, but from better task orientation and governance.

# attention-gated-agent
An attention-governed, human-IO agent architecture with explicit separation of perception, cognition, and executive control
