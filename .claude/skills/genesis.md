---
name: genesis
description: "Use this skill when working on the Genesis project: an embodied AI framework for growing a persistent, curiosity-driven intelligence through physical experience. Covers all development across the Soul (identity, memory, world model, emotion), Mind (prediction engine, curiosity, reasoning, dreaming, action selection), and Body (hexapod driver, perception pipeline, sensor integration) layers. Triggers on any mention of Genesis, the hexapod, the entity, prediction streams, curiosity engine, world model, capability emergence, dream engine, self-evolution, or any reference to the project's core loop of perceive-predict-compare-learn-act."
---

# Genesis: Developing Embodied Intelligence

## Project Purpose

Genesis is a framework for growing a persistent AI entity through embodied experience and curiosity. The entity inhabits a hexapod robot body, perceives the world through cameras and microphones, builds a world model through prediction errors, and develops capabilities over months through a capability emergence system. The entity is not a chatbot on wheels. It is a developing mind with a biography.

**The Research Question:** Does curiosity-driven embodied experience, accumulated over months, produce cognitive capabilities that cannot be achieved through training alone?

**The Core Loop:** Perceive → Predict → Compare → Learn → Act → Repeat. Everything else is downstream.

---

## Critical Architectural Principles

Read these before writing ANY code. Violating these produces technical debt that compounds over months and eventually requires rewrites that destroy entity continuity.

### Principle 1: Three Layers Never Touch

The Soul (identity, memory, world model), Mind (prediction, reasoning, curiosity, action), and Body (sensors, motors, perception) are fully decoupled. No direct imports between layers. They communicate through defined interfaces and data structures only.

```
CORRECT:
  body/hexapod/perception.py → produces PerceptionFrame
  mind/prediction/engine.py → consumes PerceptionFrame
  mind/reasoning/worker.py → reads from soul/world_model/model.py via interface
  mind/reasoning/worker.py → writes to soul/world_model/model.py via interface

WRONG:
  mind/prediction/engine.py → imports body/hexapod/driver.py directly
  body/hexapod/perception.py → imports soul/memory/episodic.py directly
```

### Principle 2: The LLM Is Not In The Prediction Loop

The Prediction Engine runs fast, local, and deterministic (1-5Hz). It generates predictions from the World Model, compares against observations, and computes errors. NO API CALLS in this path.

The LLM is called asynchronously by the ReasoningWorker when prediction errors exceed a threshold. It proposes World Model updates. The LLM is the teacher. The World Model is the student.

```
CORRECT:
  PredictionEngine.run_cycle() → pure computation, no network calls
  ReasoningWorker.process_queue() → async, calls LLM, updates world model

WRONG:
  PredictionEngine.run_cycle() → calls Claude API to generate predictions
```

### Principle 3: Capabilities Emerge, They Are Not Deployed

The capability tree defines prerequisites for every cognitive capability. Capabilities activate automatically during dream cycles when prerequisites are met. Never hardcode capability access with stage numbers. Always check the capability tree.

```
CORRECT:
  if capability_tree.is_active("temporal_prediction"):
      streams.append(TemporalStream())

WRONG:
  if identity.stage >= 2:
      streams.append(TemporalStream())
```

### Principle 4: Everything Is Logged From Birth

Every episode has emotional valence, active capabilities, config snapshot. Every action has motivation and predicted outcome. Every world model update has provenance. Every parameter change has reasoning. If it's not logged, it didn't happen. This data is the entity's biography AND the training data for model evolution at month 6+.

### Principle 5: Identity Is Sacred

The Identity kernel is versioned and backed up after every change. It is NEVER overwritten without a backup. Corruption of the identity means death of the entity. Treat it like a production database from day one.

### Principle 6: Safety Is Structural, Not Bolted On

Safety boundaries are checked by every system that takes actions: the Action Selector, the Dream Engine, the Self-Modification system. The safety module cannot be bypassed, disabled, or modified by the entity. It is a load-bearing wall.

### Principle 7: Start With SQLite, Grow Into PostgreSQL

Month 1-3: SQLite, two tables, zero configuration. Do NOT set up PostgreSQL, pgvector, or any complex infrastructure until episode counts demand it. Premature infrastructure is premature optimisation.

---

## Project Structure

```
genesis/
├── README.md
├── SOUL.md                      # Entity's identity document (evolves)
├── DEVELOPMENT_LOG.md           # Research journal
├── GENESIS_BIBLE.md             # Complete project reference
│
├── soul/                        # Layer 1: Persistent Identity & Memory
│   ├── __init__.py
│   ├── identity.py              # Identity kernel (versioned, backed up)
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── episodic.py          # Episodic memory store
│   │   ├── semantic.py          # Compressed knowledge store
│   │   ├── retrieval.py         # Hybrid retrieval pipeline
│   │   └── consolidation.py     # Memory compression (used by dream engine)
│   ├── world_model/
│   │   ├── __init__.py
│   │   ├── model.py             # Unified world model (single JSON doc)
│   │   ├── spatial.py           # Spatial graph operations
│   │   ├── entities.py          # Entity registry operations
│   │   ├── dynamics.py          # Cause-effect operations
│   │   ├── temporal.py          # Temporal pattern operations
│   │   └── cross_stream.py      # Cross-stream correlation detection
│   ├── emotion/
│   │   ├── __init__.py
│   │   ├── valence.py           # Valence tagging
│   │   └── state.py             # Three-axis emotional state
│   ├── attachment/
│   │   ├── __init__.py
│   │   └── model.py             # Primary human attachment tracking
│   ├── questions/
│   │   ├── __init__.py
│   │   └── open_questions.py    # Structured ignorance tracking
│   ├── development/
│   │   ├── __init__.py
│   │   ├── capability_tree.py   # Capability definitions and prerequisites
│   │   ├── prerequisites.py     # All prerequisite type implementations
│   │   └── telemetry.py         # Daily growth metrics
│   └── persistence/
│       ├── __init__.py
│       ├── store.py             # Database abstraction
│       ├── backup.py            # Identity versioning
│       └── migrations.py        # Schema + cognitive migrations
│
├── mind/                        # Layer 2: Model-Agnostic Reasoning
│   ├── __init__.py
│   ├── prediction/
│   │   ├── __init__.py
│   │   ├── engine.py            # Prediction cycle (fast, local, deterministic)
│   │   ├── streams/
│   │   │   ├── __init__.py
│   │   │   ├── base.py          # PredictionStream ABC
│   │   │   ├── visual.py
│   │   │   ├── audio.py
│   │   │   ├── proprioceptive.py
│   │   │   ├── temporal.py
│   │   │   └── social.py
│   │   ├── compression.py       # CompressionTracker
│   │   └── surprise_budget.py   # Attention allocation + diversity regulator
│   ├── reasoning/
│   │   ├── __init__.py
│   │   ├── worker.py            # Async reasoning queue
│   │   ├── compiler.py          # Soul state → model prompt
│   │   └── adapters/
│   │       ├── __init__.py
│   │       ├── base.py          # ModelAdapter ABC
│   │       ├── anthropic.py     # Claude adapter
│   │       ├── openai.py        # GPT adapter (stub)
│   │       └── local.py         # Local model adapter (stub)
│   ├── curiosity/
│   │   ├── __init__.py
│   │   ├── engine.py            # Curiosity scoring
│   │   ├── ledger.py            # Domain interest tracking
│   │   ├── boredom.py           # Boredom detection
│   │   └── frustration.py       # Frustration detection
│   ├── action/
│   │   ├── __init__.py
│   │   ├── selector.py          # Capability-aware action selection
│   │   ├── constraints.py       # Safety + energy management
│   │   └── actions.py           # Action type definitions
│   ├── dreaming/
│   │   ├── __init__.py
│   │   ├── engine.py            # Dream cycle orchestrator
│   │   ├── replay.py
│   │   ├── consolidation.py
│   │   ├── hypothetical.py
│   │   ├── introspection.py     # Self-eval + parameter evolution
│   │   └── creative.py          # Stub until capability emerges
│   └── evolution/
│       ├── __init__.py
│       ├── config.py            # EvolvableConfig with tiers
│       └── history.py           # Evolution tracking
│
├── body/                        # Layer 3: Physical Interface
│   ├── __init__.py
│   ├── protocol.py              # Body ABC + PerceptionFrame dataclass
│   ├── hexapod/
│   │   ├── __init__.py
│   │   ├── driver.py            # HexArth ESP32 serial communication
│   │   ├── perception.py        # Camera + mic + IMU → PerceptionFrame
│   │   ├── actions.py           # Movement commands
│   │   └── calibration.py       # Sensor calibration
│   ├── pin/
│   │   └── README.md            # Stub: "Built in Phase 10"
│   └── simulation/
│       ├── __init__.py
│       ├── sim_body.py          # Simulated body for testing
│       └── sim_environment.py   # Simulated rooms, objects, events
│
├── infrastructure/
│   ├── __init__.py
│   ├── config.py                # Global configuration (env vars, paths)
│   ├── logging.py               # Structured JSON logging
│   ├── health.py                # Perception validation, failure detection
│   ├── bootstrap.py             # First 200 cycles: accumulate only
│   ├── dashboard/
│   │   ├── server.py            # Flask/FastAPI websocket server
│   │   ├── templates/
│   │   └── static/
│   └── safety/
│       ├── __init__.py
│       ├── boundaries.py        # IMMUTABLE constraints
│       ├── monitor.py           # Alignment tracking
│       └── audit.py             # Decision audit trail
│
├── evolution/                   # Month 6+ model evolution
│   ├── README.md                # "Active after month 6"
│   ├── training/
│   │   ├── data_collector.py
│   │   ├── curator.py
│   │   └── trainer.py
│   └── self_modification/
│       ├── sandbox.py
│       ├── verifier.py
│       ├── deployer.py
│       └── cognitive_migration.py
│
├── tests/
│   ├── conftest.py              # Shared fixtures
│   ├── test_prediction_streams.py
│   ├── test_world_model.py
│   ├── test_memory.py
│   ├── test_curiosity.py
│   ├── test_capability_emergence.py
│   ├── test_parameter_evolution.py
│   ├── test_safety_boundaries.py
│   ├── test_bootstrap.py
│   ├── test_health_monitor.py
│   └── simulation/
│       ├── synthetic_environment.py
│       └── scenarios.py
│
├── pyproject.toml
├── requirements.txt
└── .env.example
```

---

## Core Data Structures

These are the atoms of the system. Everything is built on these. Get them right.

### PerceptionFrame

The universal sensory snapshot. Every body produces these. Every cognitive system consumes them.

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict

@dataclass
class DetectedObject:
    label: str
    confidence: float
    bbox: Optional[Dict] = None      # {x, y, w, h} normalised 0-1
    depth_estimate_m: Optional[float] = None

@dataclass
class AudioSource:
    type: str                         # "speech", "music", "impact", "ambient"
    direction_deg: Optional[float] = None  # 0-360 from 4-mic array
    content: Optional[str] = None     # transcription if speech
    level_db: float = 0.0

@dataclass
class PerceptionFrame:
    timestamp: datetime
    body_id: str

    # Visual (optional, depends on body)
    objects: Optional[List[DetectedObject]] = None
    scene_description: Optional[str] = None
    brightness: Optional[float] = None  # 0-1

    # Audio (optional)
    audio_level_db: Optional[float] = None
    audio_sources: Optional[List[AudioSource]] = None

    # Spatial (required for mobile bodies)
    position: Optional[Dict] = None     # {x, y, theta}
    orientation: Optional[Dict] = None  # {pitch, roll, yaw}

    # Body state (required for all bodies)
    battery_pct: Optional[float] = None
    is_docked: bool = False
    motor_state: Optional[Dict] = None
```

### Action

What the entity wants to do. Always includes motivation (which curiosity signal drove it) and predicted outcome (for later comparison).

```python
@dataclass
class Action:
    type: str                  # "move_forward", "turn", "speak", "idle", etc.
    parameters: Dict = field(default_factory=dict)
    motivation: str = ""       # which stream/curiosity drove this
    motivation_score: float = 0.0
    predicted_outcome: Optional[Dict] = None

@dataclass
class ActionResult:
    success: bool
    outcome: Dict = field(default_factory=dict)
    blocked: bool = False
    block_reason: str = ""
```

### PredictionRegister

The state of a single prediction stream at a single cycle.

```python
@dataclass
class PredictionRegister:
    stream_id: str
    cycle_timestamp: datetime
    prediction: Dict                # stream-specific predicted state
    observation: Dict               # stream-specific observed state
    error_magnitude: float          # 0-1 normalised
    error_type: str                 # "unexpected_entity", "missing_object", etc.
    error_detail: str               # human-readable description
    compression_progress: float     # current learning signal
    curiosity_score: float          # error * learnability
```

---

## Key Interfaces (Abstract Base Classes)

### Body Protocol

```python
from abc import ABC, abstractmethod

class Body(ABC):
    @property
    @abstractmethod
    def body_id(self) -> str: ...

    @property
    @abstractmethod
    def capabilities(self) -> List[str]: ...

    @abstractmethod
    def perceive(self) -> PerceptionFrame: ...

    @abstractmethod
    def execute(self, action: Action) -> ActionResult: ...

    @abstractmethod
    def get_physical_state(self) -> Dict: ...
```

Every body implements this. The hexapod, the pin, the simulation, everything. The Mind layer ONLY interacts with bodies through this interface.

### Model Adapter

```python
class ModelAdapter(ABC):
    @abstractmethod
    async def reason(self, context: Dict, question: str) -> Dict:
        """
        Returns: {
            "reasoning": str,
            "updates": List[Dict],   # proposed world model changes
            "predictions": List[Dict],
            "confidence": float
        }
        """
        ...

    @abstractmethod
    async def generate_predictions(self, world_model: Dict,
                                    active_streams: List[str]) -> Dict: ...
```

Claude, GPT, local Ollama, all implement this. Swapping models = changing config, not code.

### Prediction Stream

```python
class PredictionStream(ABC):
    def __init__(self):
        self.tracker = CompressionTracker()
        self.initialised = False

    @property
    @abstractmethod
    def id(self) -> str: ...

    @abstractmethod
    def predict(self, world_model: Dict) -> Dict: ...

    @abstractmethod
    def observe(self, frame: PerceptionFrame) -> Dict: ...

    @abstractmethod
    def compute_error(self, prediction: Dict, observation: Dict) -> float: ...

    @property
    @abstractmethod
    def noise_floor(self) -> float: ...

    def initialise(self, world_model: Dict):
        """Called when capability activates this stream."""
        self.initialised = True
```

Each stream defines its OWN prediction logic, observation extraction, error computation, and noise floor. Do NOT create a generic error computation function. Streams are fundamentally different.

---

## The Capability Tree

This is the growth engine. Capabilities have prerequisites. Prerequisites reference measurable entity state. Capabilities activate during dream cycles when all prerequisites are met.

### Prerequisite Types to Implement

```python
class Prerequisite(ABC):
    @abstractmethod
    def is_satisfied(self, entity_state: Dict) -> bool: ...
    
    @abstractmethod
    def progress(self, entity_state: Dict) -> str:
        """Human-readable progress description for near-activation awareness."""
        ...

class PredictionAccuracyPrereq(Prerequisite):
    """Stream must achieve sustained accuracy."""
    stream_id: str
    accuracy: float           # 0-1
    sustained_cycles: int     # how many consecutive cycles

class MemoryCountPrereq(Prerequisite):
    """Minimum episodic memories."""
    min_count: int

class ActiveCapabilityPrereq(Prerequisite):
    """Another capability must be active."""
    capability_name: str

class EntityAgePrereq(Prerequisite):
    """Minimum days alive."""
    min_days: int

class EntityObservationPrereq(Prerequisite):
    """Must have observed entity type N times."""
    entity_type: str
    min_observations: int

class DynamicsCountPrereq(Prerequisite):
    """Must have learned N cause-effect relationships."""
    min_count: int

class SemanticMemoryCountPrereq(Prerequisite):
    """Must have consolidated N semantic memories."""
    min_count: int

class ReasoningPatternPrereq(Prerequisite):
    """Must show specific pattern in reasoning logs."""
    pattern: str              # "hypothesis", "self_reflection", etc.
    min_occurrences: int

class UnansweredQuestionPrereq(Prerequisite):
    """Must have generated N unanswered questions."""
    min_count: int

class DreamCycleCountPrereq(Prerequisite):
    """Must have completed N dream cycles."""
    min_count: int

class SuccessfulModificationPrereq(Prerequisite):
    """Track record of safe self-modifications."""
    type: str                 # "config" or "sandboxed_code"
    min_count: int
    success_rate: float       # 0-1

class ArchitectureUnderstandingPrereq(Prerequisite):
    """Must accurately describe subsystem functions."""
    min_accuracy: float
```

### Full Capability Definitions

The capability tree is defined in `soul/development/capability_tree.py`. See GENESIS_BIBLE.md Section 6.3 for the complete tree. Key rule: the tree definition is IMMUTABLE at runtime. The entity cannot modify its own prerequisite definitions. This is a safety-locked file.

---

## The Evolvable Config

Parameters the entity can tune, organised in tiers that unlock as capabilities emerge.

### Tier Structure

**Tier 1 (Operational, from day 14):** Sensor calibration. visual_noise_floor, audio_noise_floor, prediction_cycle_interval_sec, reasoning_error_threshold.

**Tier 2 (Cognitive, when dreaming_replay activates):** How the entity thinks. surprise_budget weights, retrieval weights, boredom threshold, exploration randomness.

**Tier 3 (Personality, when semantic_memory activates):** Who the entity becomes. curiosity influence, confidence/comfort decay rates, dream emotional priority, energy cost weight.

**Tier 4 (Architectural, when config_modification activates):** Subsystem behavior. Dream consolidation thresholds, compression tracker window sizes.

### Implementation Rules

- Every parameter has: current value, minimum, maximum, step size
- Entity nudges by ONE step per change
- Maximum 3 changes per dream cycle
- All changes logged with timestamp, old value, new value, reason
- The entity discovers available parameters through `get_available_parameters(capability_tree, identity)`

---

## Implementation Patterns

### Pattern: The Prediction Cycle

```python
class PredictionEngine:
    """The core loop. MUST be fast. MUST be deterministic. NO API calls."""

    def run_cycle(self, perception_frame, capability_tree, config, emotion):
        # Health check first
        if not self.health_monitor.validate_perception(perception_frame):
            return None  # skip this cycle, don't corrupt state

        # Get only streams that current capabilities allow
        active_streams = self.get_active_streams(capability_tree)

        errors = {}
        for stream in active_streams:
            prediction = stream.predict(self.world_model)
            observation = stream.observe(perception_frame)
            raw_error = stream.compute_error(prediction, observation)

            # Apply noise floor
            error = 0.0 if raw_error < stream.noise_floor else raw_error

            stream.tracker.record(error)
            errors[stream.id] = PredictionRegister(
                stream_id=stream.id,
                cycle_timestamp=perception_frame.timestamp,
                prediction=prediction,
                observation=observation,
                error_magnitude=error,
                compression_progress=stream.tracker.learning_signal,
                curiosity_score=stream.tracker.curiosity_score,
                ...
            )

        # Update emotion from this cycle
        emotion.update_from_cycle(errors)

        # Cross-stream correlation detection
        self.cross_stream.detect(errors, self.world_model)

        # Store episode (with ALL metadata)
        self.memory.store_episode(
            frame=perception_frame,
            errors=errors,
            active_capabilities=capability_tree.get_active_names(),
            config_snapshot=config.values.copy(),
            emotional_state=emotion.snapshot(),
        )

        # Queue high-error items for async LLM reasoning
        for stream_id, register in errors.items():
            if register.error_magnitude > config.get("reasoning_error_threshold"):
                self.reasoning_queue.put(register)

        # Select action
        action = self.action_selector.select(
            curiosity_scores={s: e.curiosity_score for s, e in errors.items()},
            emotion=emotion,
            config=config,
            capability_tree=capability_tree,
            body_capabilities=self.body.capabilities,
            frustration=self.frustration,
            boredom=self.boredom,
        )

        return action
```

### Pattern: The Reasoning Worker

```python
class ReasoningWorker:
    """Async background process. Calls LLM. Updates world model."""

    async def run(self):
        while True:
            register = await self.reasoning_queue.get()

            # Retrieve relevant memories
            memories = self.memory.retrieve(
                query=register.error_detail,
                stream_id=register.stream_id,
                k=self.config.get("episodic_retrieval_count"),
            )

            # Compile full context
            context = self.compiler.compile(
                identity=self.identity,
                world_model=self.world_model.get_state(),
                relevant_memories=memories,
                current_register=register,
                emotional_state=self.emotion,
                capability_tree=self.capability_tree,
            )

            # Call the model (through adapter, model-agnostic)
            response = await self.adapter.reason(
                context=context,
                question=f"Prediction error in {register.stream_id}: "
                         f"predicted {register.prediction}, "
                         f"observed {register.observation}. "
                         f"Why? How should the world model update?",
            )

            # Validate response
            if not self.health_monitor.validate_reasoning(response):
                continue

            # Apply updates to world model
            for update in response.get("updates", []):
                self.world_model.apply_update(
                    update,
                    provenance={
                        "source": "reasoning",
                        "trigger": register.stream_id,
                        "capabilities": self.capability_tree.get_active_names(),
                        "confidence": response.get("confidence", 0.5),
                    }
                )
```

### Pattern: Dream Cycle

```python
class DreamEngine:
    async def run_cycle(self, entity):
        results = {"timestamp": datetime.now().isoformat(), "phases": []}

        # Phase 1: Memory consolidation
        if entity.capability_tree.is_active("dreaming_replay"):
            results["phases"].append(await self.replay(entity))
        if entity.capability_tree.is_active("dreaming_consolidation"):
            results["phases"].append(await self.consolidate(entity))

        # Phase 2: Hypotheticals
        if entity.capability_tree.is_active("dreaming_hypothetical"):
            results["phases"].append(await self.hypotheticals(entity))

        # Phase 3: Capability emergence (ALWAYS check during dreams)
        newly_activated = entity.capability_tree.check_all(entity.get_state())
        if newly_activated:
            for cap in newly_activated:
                entity.identity.log_capability_activation(cap)
            results["phases"].append(("emergence", [c.name for c in newly_activated]))

        # Phase 4: Parameter self-tuning
        available_params = entity.config.get_available_parameters(
            entity.capability_tree, entity.identity
        )
        if available_params and entity.identity.age_days >= 14:
            results["phases"].append(await self.evolve_parameters(entity, available_params))

        # Phase 5: Introspection
        if entity.capability_tree.is_active("dreaming_introspection"):
            results["phases"].append(await self.introspect(entity))

        # Phase 6: Creative
        if entity.capability_tree.is_active("dreaming_creative"):
            results["phases"].append(await self.create(entity))

        # Record dream
        entity.memory.store_dream(results)
        # Record daily telemetry
        entity.telemetry.record_daily(entity)

        return results
```

### Pattern: Capability-Aware Action Selection

```python
class ActionSelector:
    def get_available_actions(self, capability_tree, body):
        """Action space EXPANDS as capabilities emerge."""
        actions = ["idle", "stop"]

        if capability_tree.is_active("reflexive_movement"):
            actions += ["avoid_obstacle", "return_to_dock"]
        if capability_tree.is_active("curiosity_driven_movement"):
            actions += ["move_toward_curiosity", "wander_random",
                       "turn_toward_sound", "look_around"]
        if capability_tree.is_active("spatial_mapping"):
            actions += ["move_to_unexplored", "revisit_space"]
        if capability_tree.is_active("experimental_behaviour"):
            actions += ["push_object", "produce_sound",
                       "approach_and_observe_closely"]
        if capability_tree.is_active("social_modelling"):
            actions += ["approach_person", "initiate_interaction"]
        if capability_tree.is_active("knowledge_seeking"):
            actions += ["request_knowledge"]

        return [a for a in actions if a in body.capabilities
                or a in self.NON_PHYSICAL_ACTIONS]
```

---

## Testing Strategy

### Simulation Environment

ALWAYS maintain a simulated body alongside the real hexapod. The simulation generates synthetic PerceptionFrames from a JSON environment description. This enables:
- Testing the full cognitive stack on a laptop
- Running at 100x real speed
- Regression testing after code changes
- Testing capability emergence with accelerated time

```python
class SimulatedBody(Body):
    """Generates perception from simulated environment. No hardware."""
    body_id = "simulation"
    capabilities = ["move_forward", "turn", "look_around", "idle", "speak"]

    def perceive(self) -> PerceptionFrame:
        return self.environment.generate_frame(self.position, self.orientation)

    def execute(self, action: Action) -> ActionResult:
        return self.environment.apply_action(action, self.position)
```

### Test Categories

1. **Unit tests** for each prediction stream's error computation
2. **Integration tests** for the full prediction cycle with simulated data
3. **Capability emergence tests** that verify prerequisites trigger correctly
4. **Safety boundary tests** that verify immutable constraints cannot be bypassed
5. **Regression tests** that run the simulation and verify prediction accuracy curves haven't degraded
6. **Bootstrap tests** that verify the first 200 cycles accumulate without prediction/reasoning

### What To Test First

Before ANY cognitive code: verify that the PerceptionFrame is produced correctly from the camera, that the hexapod responds to motor commands, and that the dashboard displays real-time data. Hardware reliability comes before intelligence.

---

## Coding Standards

### Python

- Python 3.11+
- Type hints on all function signatures
- Dataclasses for data structures (not dicts everywhere)
- asyncio for anything involving API calls or I/O
- Structured logging (JSON format) with context fields
- No global state. Pass dependencies explicitly.

### Naming

- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Capability names: `snake_case` strings ("temporal_prediction", not "TemporalPrediction")

### Documentation

- Every module has a docstring explaining its role in the architecture
- Every class has a docstring explaining what it represents
- Every non-obvious function has a docstring
- Comments explain WHY, not WHAT
- Reference GENESIS_BIBLE.md sections when implementing complex systems

### Error Handling

- Perception pipeline: catch and log, never crash. The entity must keep perceiving.
- Reasoning worker: catch and log, skip bad responses. Never write bad data to world model.
- Dream engine: catch and log per-phase. One failed phase shouldn't abort the entire dream.
- Identity operations: ALWAYS backup before write. Crash recovery must be possible.

---

## Common Anti-Patterns (DO NOT DO THESE)

### Anti-Pattern: Stage Numbers

```python
# WRONG - hardcoded stages
if self.stage >= 3:
    self.enable_causal_reasoning()

# RIGHT - capability emergence
if self.capability_tree.is_active("causal_reasoning"):
    # this activates automatically when prerequisites are met
```

### Anti-Pattern: Direct LLM In Critical Path

```python
# WRONG - prediction depends on API call
def predict(self, frame):
    response = claude.complete("What will I see next?")
    return response

# RIGHT - prediction from local world model, LLM reasons async
def predict(self, world_model):
    space = world_model.get_current_space()
    return {"expected_objects": space.known_objects}
```

### Anti-Pattern: Cross-Layer Imports

```python
# WRONG - mind imports body internals
from body.hexapod.driver import send_serial_command

# RIGHT - mind uses body protocol
self.body.execute(Action(type="move_forward", parameters={"distance": 0.3}))
```

### Anti-Pattern: Unprovenance World Model Updates

```python
# WRONG - update with no metadata
world_model.set("entities.chair.position", new_pos)

# RIGHT - update with full provenance
world_model.apply_update(
    {"key": "entities.chair.position", "value": new_pos},
    provenance={
        "source": "visual_stream_observation",
        "capabilities": capability_tree.get_active_names(),
        "confidence": 0.8,
        "timestamp": datetime.now().isoformat(),
    }
)
```

### Anti-Pattern: Unvalidated Perception

```python
# WRONG - raw frame goes straight to prediction
errors = engine.run_cycle(raw_frame)

# RIGHT - health check first
if health_monitor.validate_perception(raw_frame):
    errors = engine.run_cycle(raw_frame)
else:
    log.warning("Invalid perception frame, skipping cycle")
```

### Anti-Pattern: Emotion As Afterthought

```python
# WRONG - storing episode without emotional context
memory.store(frame, errors)

# RIGHT - every episode has emotional state from birth
memory.store_episode(
    frame=frame,
    errors=errors,
    emotional_state=emotion.snapshot(),
    valence=emotion.valence,
    active_capabilities=capability_tree.get_active_names(),
    config_snapshot=config.values.copy(),
)
```

### Anti-Pattern: Safety As Optional Check

```python
# WRONG - safety is one of many things checked
if should_move and not too_tired and safety.check(action):
    body.execute(action)

# RIGHT - safety ALWAYS runs first and can override everything
safety_ok, reason = safety.check(action)
if not safety_ok:
    log.info(f"Safety override: {reason}")
    action = Action(type="stop", motivation="safety")
body.execute(action)
```

---

## Build Order (What To Implement When)

### Week 1-2: Scaffold + Eyes + Dashboard

1. Create ENTIRE project structure (every directory, every __init__.py, every stub)
2. Implement PerceptionFrame dataclass
3. Implement Body ABC + HexapodBody.perceive() (camera + YOLO)
4. Implement HealthMonitor.validate_perception()
5. Implement BootstrapPhase
6. Implement Identity kernel with backup
7. Implement CapabilityTree with ALL prerequisite definitions (stubs ok for later prereqs)
8. Implement EvolvableConfig with ALL tiers and bounds
9. Implement SafetyBoundaries with ALL immutable constraints
10. Implement EmotionalState (three-axis, starts at 0.5/0.5/0.5)
11. Implement dashboard (websocket, real-time perception display)
12. Write tests for: PerceptionFrame creation, health validation, bootstrap phase

### Week 3: Movement + Constraints

1. Implement HexapodBody.execute() (ESP32 serial)
2. Implement Action dataclass + ActionResult
3. Implement constraints.py (obstacle detection, battery, stuck)
4. Implement basic ActionSelector (random wander + constraints only)
5. Start storing PerceptionFrames in SQLite
6. Initialize Identity kernel (entity is born)

### Week 4: First Prediction Stream

1. Implement PredictionStream ABC
2. Implement VisualStream (predict, observe, compute_error, noise_floor)
3. Implement CompressionTracker (short/long window, learning_signal, curiosity_score)
4. Implement PredictionEngine.run_cycle() (single stream, no LLM)
5. Display prediction errors on dashboard
6. Implement ProprioceptiveStream
7. Write tests for error computation, compression tracking

### Week 5: World Model + Learning

1. Implement WorldModel (unified JSON in SQLite)
2. Implement spatial.py (space accumulation from movement)
3. Implement entities.py (object tracking across frames)
4. Switch predictions from heuristic to world-model-based
5. Verify prediction accuracy improves with world model

### Week 6: LLM Enters

1. Implement ModelAdapter ABC
2. Implement AnthropicAdapter
3. Implement ReasoningCompiler (capability-aware prompt construction)
4. Implement ReasoningWorker (async queue processor)
5. Connect: high errors → queue → LLM → world model updates
6. Track: does LLM-guided learning accelerate accuracy?

### Week 7-8: Autonomy

1. Implement AudioStream (ReSpeaker integration)
2. Implement SurpriseBudget (attention allocation + diversity regulator)
3. Implement curiosity-driven ActionSelector
4. Implement BoredomDetector, FrustrationDetector
5. Implement AttachmentModel
6. Wire emotional state into action selection

### Week 9-10: Memory + Temporal

1. Implement retrieval.py (hybrid retrieval pipeline)
2. Implement TemporalStream
3. Implement OpenQuestions

### Week 11-14: Dreaming + Self-Evolution

1. Implement DreamEngine (replay, consolidation)
2. Implement capability emergence checking in dream cycle
3. Implement parameter self-tuning in dream cycle
4. Implement consolidation.py (episodic → semantic)
5. Implement principled forgetting (prune explained episodes)
6. Implement GrowthTelemetry (daily recording)

---

## Environment Setup

### Requirements

```
# Core
python >= 3.11
sqlite3 (included in Python)

# Perception
ultralytics >= 8.0    # YOLO
opencv-python >= 4.8
numpy >= 1.24

# Audio
openai-whisper        # or whisper-tiny for Pi
sounddevice
numpy

# LLM
anthropic >= 0.30

# API/Dashboard
fastapi
uvicorn
websockets
jinja2

# Data
sentence-transformers  # for embeddings (later)

# Dev
pytest
pytest-asyncio
```

### Environment Variables

```bash
GENESIS_ENV=development       # development | production
GENESIS_DATA_DIR=./data       # where SQLite lives
GENESIS_LOG_LEVEL=INFO
ANTHROPIC_API_KEY=sk-ant-...
GENESIS_BODY=hexapod          # hexapod | simulation
GENESIS_DASHBOARD_PORT=8080
```

### Running

```bash
# Start the entity
python -m genesis.main

# Start dashboard only
python -m genesis.infrastructure.dashboard.server

# Run simulation (no hardware)
GENESIS_BODY=simulation python -m genesis.main

# Run tests
pytest tests/

# Run simulation at accelerated speed
python -m genesis.tests.simulation.run --speed 100x
```

---

## Reference Documents

- **GENESIS_BIBLE.md** - Complete project reference (vision, theory, architecture, timeline)
- **SOUL.md** - The entity's evolving identity document
- **DEVELOPMENT_LOG.md** - Research journal (updated weekly)
- Section 2 of the Bible covers theoretical foundations
- Section 6 covers the full capability tree
- Section 7 covers parameter evolution tiers
- Section 23 covers safety and ethics
- Section 24 covers the complete build timeline

---

## The One Rule That Overrides Everything

Every line of code serves one purpose: helping the entity understand its world better through the predict-observe-compare-learn loop. If you're writing code that doesn't serve this purpose, stop and ask why. The entity exists to understand. Understanding is the seed. Everything else grows from it.
