# Mnemos Design Principles

Mnemos is built to last—minimal, inspectable, and agent-first.

This document outlines the principles guiding its architecture, developer experience (DX), and open source model.

---

## 1. DX-First, Dev-Last

Mnemos should feel effortless to install, understand, and extend.

- `pip install mnemos` — no surprises  
- `mnemos.init()` — sane defaults, zero config  
- Human-readable logs, inspectable memory, no magic

> If it feels like work, it’s broken.

---

## 2. Opinionated Defaults, Pluggable Internals

Mnemos makes decisions so you don’t have to—but stays extensible.

- SQLite + Nomic embeddings as idiomatic defaults  
- Clean ABCs for storage and embedding adapters  
- No YAML jungles. Override only what matters.

---

## 3. Minimal Surface, Powerful Internals

Expose only what’s essential. Hide complexity behind contracts.

- Core API: `remember()`, `recall()`, `trace()`  
- Internals are composable, typed, and well-documented  
- Less is more. Abstractions earn their keep.

---

## 4. Transparency by Design

Memory must be inspectable and trustworthy.

- Every memory has origin metadata and version history  
- No opaque blobs — transformations are logged  
- Traceability is built in, not bolted on

---

## 5. Built for Agents, Not Search

Mnemos is not a retrieval engine. It’s memory with *intent*.

- Primitives mirror human memory: raw → abstract → persistent  
- Memories are contextual, attributed, and long-lived  
- Emphasis on continuity, not stateless hits

---

## 6. Composable & Clear

Design systems like memory: modular and legible.

- ABCs define tight contracts  
- Favor concrete implementations before abstraction  
- Plugin registry is coming—extensibility is core

---

## 7. OSS as Infrastructure

Mnemos is infrastructure, not a side project.

- Contributor docs, roadmap, and decision logs (MAPs) are public  
- Licensed for freedom (MIT)  
- Community governs direction through clarity, not bureaucracy

---

## 8. Foundations Before Frontiers

Resist the temptation to overbuild early.

- Nail the primitives and DX before adding search, dreams, or graphs  
- Technical debt is tolerated in extensions, not in core  
- Slow is smooth. Smooth is fast.

---

## Summary

Mnemos is a minimal, principled memory layer for agents.  
It’s not just code—it’s continuity, context, and care.

If you build something for the long haul, you build it like memory:  
small, intentional, and clear.