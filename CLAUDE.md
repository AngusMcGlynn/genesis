# Genesis - Embodied AI Framework

## MANDATORY: Read Before Every Task
Read docs/SKILL.md before writing any code. It contains the architecture, data structures, interfaces, patterns, anti-patterns, and build order.

Read docs/GENESIS_BIBLE.md for complete project context (theory, capability tree definitions, parameter tiers, safety constraints, hardware specs, monetisation, competitive positioning).

## Architecture Overview
Genesis grows a persistent AI entity through embodied experience and curiosity. Three layers, fully decoupled:
- **Soul** (soul/): Identity, memory, world model, emotion, attachment, capability tree. Persistent. Never reset.
- **Mind** (mind/): Prediction engine, curiosity, reasoning, action selection, dreaming, evolution. Model-agnostic. Interchangeable.
- **Body** (body/): Sensors, motors, perception pipeline. Modular. Multiple bodies, one identity.

## Core Rules

### Layer Isolation
- soul/, mind/, body/ NEVER import each other directly
- They communicate through defined interfaces and data structures only
- body/ produces PerceptionFrame. mind/ consumes it. mind/ reads/writes soul/ through interfaces.

### The Prediction Loop
- PredictionEngine.run_cycle() is FAST, LOCAL, DETERMINISTIC. No API calls. No async. No network.
- Predictions come from the World Model, not the LLM.
- The LLM is called asynchronously by ReasoningWorker when prediction errors exceed threshold.
- The LLM proposes World Model updates. The LLM is the teacher. The World Model is the student.

### Three-Speed Mind
- **Fast brain** (50-100ms): Pi locally. YOLO + rules. Obstacle avoidance, reflexes. No API.
- **Medium brain** (1-2s): Navigation decisions, spatial context. Light reasoning.
- **Slow brain** (5-10s): Cloud API (Claude). Deep reasoning, world model updates, curiosity scoring, planning.
- The slow brain sets intentions. The medium brain translates to navigation. The fast brain handles safety.
- Each layer can override the one above it.

### Capability Emergence
- NEVER use stage numbers. No `if stage >= 3`. Always use `capability_tree.is_active("capability_name")`.
- Capabilities activate during dream cycles when prerequisites are met. Not manually deployed.
- The capability tree definitions are IMMUTABLE at runtime. The entity cannot modify its own prerequisites.

### Episode Logging
- Every episode MUST include: perception, errors, emotional_state, active_capabilities, config_snapshot, valence.
- Every action MUST include: motivation, motivation_score, predicted_outcome.
- Every world model update MUST include: provenance (source, capabilities, confidence, timestamp).
- If it's not logged, it didn't happen. This data is the entity's biography AND training data for model evolution.

### Identity Safety
- Identity kernel is versioned and backed up BEFORE every write. No exceptions.
- Corruption of identity = death of the entity. Treat it like a production database from day one.

### Safety Boundaries
- Safety is checked FIRST in every action path. Not one of many checks. THE FIRST check.
- SafetyBoundaries class has NO setters, NO disable method, NO unlock method.
- Immutable constraints: battery 15% emergency return, max speed 0.3m/s, obstacle min 0.15m, API rate limits.
- Locked systems: safety system, identity backup, capability tree definitions.

### Infrastructure
- SQLite for months 1-3. No PostgreSQL, no pgvector, no premature infrastructure.
- Python 3.11+, type hints everywhere, dataclasses for data structures, asyncio for I/O.
- Structured JSON logging with context fields.

## Known Drift Patterns
_Add violations here as you catch them during development:_

- DO NOT call any API in PredictionEngine.run_cycle(). Predictions are LOCAL.
- DO NOT use stage numbers anywhere. Always check capability_tree.is_active().
- DO NOT skip emotional_state or config_snapshot when storing episodes.
- DO NOT import across layers (soul/, mind/, body/ are isolated).
- DO NOT store episodes without valence tags. Emotion is wired in from birth.
- DO NOT skip health validation before perception enters cognitive layers.
- DO NOT write to identity without calling backup() first.
- DO NOT add PostgreSQL, pgvector, or vector search until episode count demands it (month 3+).

## Key References
- `docs/SKILL.md` - Technical architecture, data structures, interfaces, patterns, anti-patterns, build order
- `docs/GENESIS_BIBLE.md` - Complete project reference (31 sections, 1497 lines)
- `docs/PROMPTS.md` - Surgical Claude Code prompts for each build phase
- `SOUL.md` - Entity identity document (evolves over time, starts empty)
- `DEVELOPMENT_LOG.md` - Research journal (updated weekly)
