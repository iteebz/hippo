# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2025-06-24

### Added
- Pluggable store backend architecture with `MemoryStore` ABC
- `InMemoryStore` as default in-memory implementation
- `Mnemos` class encapsulating core logic with pluggable storage
- `remember()`, `recall()` functions updated to use `Mnemos` instance
- `clear()` method for clearing stored artifacts, aiding test isolation
- Abstract test contract for all store implementations
- Comprehensive tests for new architecture