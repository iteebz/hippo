# Mnemos Roadmap

Welcome to the Mnemos development roadmap.

This document outlines the current release scope (v0.1), priorities, and near-future directions. It’s designed to keep contributors aligned, reduce scope creep, and make the vision legible to new collaborators.

---

## 🎯 Goal of v0.1

Deliver the smallest, highest-value implementation of Mnemos that proves its unique memory continuity model for agentic systems.

---

## ✅ v0.1.1 Scope (Shipped)

The following are implemented in v0.1.1:

- [ ] In-memory storage backend
- [ ] Core memory primitives: `Message`, `Summary`, `Artifact`
- [ ] High-level API: `remember()`, `recall()`, `trace()`
- [ ] Minimal schema & typing
- [ ] `mnemos.init()` setup function
- [ ] Package published to PyPI

---

## 🛠️ v0.1.2 (In Progress)

Introduce persistent local storage and foundational dev tooling

- [ ] SQLiteStorageAdapter
- [ ] CLI utilities: `mnemos trace`, `mnemos recall`
- [ ] Internal memory validation: schema + duplicate checks
- [ ] EmbeddingAdapter scaffold (no backends yet)
- [ ] Update public docs and add link to MAP-0
- [ ] Add optional tag indexing

---

## 🔭 Deferred to Future Releases

These ideas are valid, valuable, and likely—but explicitly **out of scope** for v0.1:

- Supabase / pgvector support
- Embedding backends (e.g. Nomic, OpenAI)
- Hybrid search (fuzzy + vector)
- Memory compaction / deduplication
- Artifact versioning & lineage
- Visualizations (e.g. UMAP, t-SNE)
- "Daemon Dream Cycle" (background salience refresh)
- Managed cloud service
- Plugin adapter registry

> These are tracked as issues or MAPs. Contributions welcome, but the core team is focused on foundational primitives and DX until they stabilize.

---

## 🧪 Success Criteria for v0.1

We consider v0.1 successful if:

- ✅ A new user can install Mnemos and store + recall memory in under 5 minutes
- ✅ Trace logs are readable and inspectable
- ✅ Contributors understand the architecture from a single glance at the public docs
- ✅ Memory feels structured—not opaque blobs or embedded soup

---

## 📦 Release Cadence

- v0.1.x → Local-first SDK, stable memory API
- v0.2.x → Optional persistent layers, basic CLI
- v0.3.x → Full adapter architecture, multiple backends, dev ergonomics
- v0.4+ → Research features, multi-agent memory, visual tools, hosted options

---

## 🗺️ Want to go deeper?

Explore:

- [MAP-0](../maps/map-0_memory-primitives.md) – design rationale for memory types
- [Principles](./principles.md) – how we think about structure, DX, and memory ethics
- [Contributing](./contributing.md) – how to help and what to expect

---

Mnemos is built to last—slow, minimal, and intentional.  
You don’t need everything. You just need memory you can trust.