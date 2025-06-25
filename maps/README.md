# Mnemos Architecture Proposals (MAPs)

Mnemos Architecture Proposals (MAPs) are structured design documents used to propose, discuss, and formalize significant architectural decisions in the Mnemos project.

MAPs serve as **intentional memory** - not just of what changed, but *why* it made sense at the time. They allow future contributors to trace reasoning, challenge assumptions, and evolve the system with context.

## 📜 Purpose

MAPs are used to:

- Propose architectural or philosophical changes
- Explore tradeoffs between multiple valid approaches
- Record design intent behind complex systems
- Prevent repeating decisions from lost context

## 📐 When to Use a MAP

Create a MAP when a decision is:

- **Seminal** - defines a core primitive or pattern  
- **Contentious** - has multiple valid solutions (though not strictly required)  
- **Cross-cutting** - touches multiple modules or interfaces  
- **Collaborative** - needs contributor feedback or alignment  
- **Philosophical** - reflects values like memory ethics or agent design  

> You don’t MAP a bug fix. You MAP a direction.  
>  
> Even if you have a clear, intuitive choice without competing alternatives, create a MAP to document the *why* behind the decision.
> MAPs capture an intentional record of decision, not forced debate.

## 🧱 Format

Each MAP is a markdown file named:  
**`map-<number>-<slug>.md`**

Start numbering at 0 and increment chronologically.

Each MAP must include:

```markdown
# MAP-0: Descriptive Title

- **Status**: Draft | Accepted | Rejected | Deprecated
- **Author**: Your Name
- **Created**: YYYY-MM-DD
- **Associated PRs**: (optional links)
- **Discussion**: (optional links)
```

Structure is flexible, but usually includes:
	•	Motivation
	•	Design proposal
	•	Tradeoffs / alternatives
	•	Future considerations

Keep MAPs short. Simplicity is a virtue.

## 📖 MAP Index

| ID     | Title                 | Status | Created     |
|--------|-----------------------|--------|-------------|
| MAP-0  | Memory Primitives     | Draft  | 2025-06-25  |
| MAP-1  | Adapter Contracts     | Draft  | 2025-06-25  |
| MAP-2  | Storage Persistence   | Draft  | 2025-06-25  |
| MAP-3  | Embedding Adapter     | Draft  | 2025-06-25  |
| MAP-4  | Attribution Metadata  | Draft  | 2025-06-25  |
| MAP-5  | Memory Lifecycle      | Draft  | 2025-06-25  |

## 🧭 Inspiration & Precedent

This format draws from successful RFC systems in other projects:

- [Python PEPs](https://github.com/python/peps)
- [Rust RFCs](https://github.com/rust-lang/rfcs)
- [Vite RFCs](https://github.com/vitejs/rfcs)
- [Next.js RFCs](https://github.com/vercel/next.js/tree/canary/rfcs)

## 🪶 Lightweight Process

There is no central review committee. MAPs are not gatekeeping tools.

They are a place to think in public, to record reasoning, and to make design decisions legible. A MAP may be written by a solo contributor or discussed collaboratively before a decision lands.

**The only rule:** If you pause while building and think _“There are multiple valid ways to do this, and I may regret the wrong one”_ — that’s a MAP.

## ✅ Summary

- Write a MAP for any architectural or philosophical design decision that’s non-trivial.
- Use the metadata block at the top.
- Add it to the table above.
- Keep it simple, intentional, and inspectable.