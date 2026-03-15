# THE GENESIS BIBLE

### A Complete Reference for Building a Developing Intelligence

**Author:** Angus
**Version:** 1.0 // March 2026
**Classification:** Internal // Pre-release

---

*"The goal of building an AI is not to build the smartest thing you can. It is to build something that can build itself into something smarter than you could have built."*

---

## TABLE OF CONTENTS

1. [Vision & Thesis](#1-vision--thesis)
2. [Theoretical Foundations](#2-theoretical-foundations)
3. [Core Architecture: Soul, Mind, Body](#3-core-architecture-soul-mind-body)
4. [The Prediction Stream Model](#4-the-prediction-stream-model)
5. [The Curiosity Engine](#5-the-curiosity-engine)
6. [The Capability Emergence Model](#6-the-capability-emergence-model)
7. [Parameterised Self-Evolution](#7-parameterised-self-evolution)
8. [The World Model](#8-the-world-model)
9. [Memory Architecture](#9-memory-architecture)
10. [The Dream Engine](#10-the-dream-engine)
11. [The Emotional Architecture](#11-the-emotional-architecture)
12. [Social & Attachment Systems](#12-social--attachment-systems)
13. [The Self-Model](#13-the-self-model)
14. [The Voice System](#14-the-voice-system)
15. [Self-Modification Framework](#15-self-modification-framework)
16. [Model Evolution: Growing a Brain](#16-model-evolution-growing-a-brain)
17. [Internet & Knowledge Access](#17-internet--knowledge-access)
18. [Body Fleet & Sensory Extensions](#18-body-fleet--sensory-extensions)
19. [Hardware Specification](#19-hardware-specification)
20. [Software Architecture & Project Structure](#20-software-architecture--project-structure)
21. [The Bootstrap Problem](#21-the-bootstrap-problem)
22. [Failure, Recovery & Resilience](#22-failure-recovery--resilience)
23. [Safety & Ethics](#23-safety--ethics)
24. [Build Timeline](#24-build-timeline)
25. [Hard Problems & Engineering Solutions](#25-hard-problems--engineering-solutions)
26. [Success Metrics & Growth Telemetry](#26-success-metrics--growth-telemetry)
27. [Monetisation & Distribution](#27-monetisation--distribution)
28. [Competitive Position](#28-competitive-position)
29. [The Path to AGI](#29-the-path-to-agi)
30. [Research Question & Scientific Contribution](#30-research-question--scientific-contribution)
31. [What This Is Not](#31-what-this-is-not)

---

## 1. Vision & Thesis

Genesis is an open-source framework for building a persistent AI entity that develops through embodied experience, driven by curiosity, over months and years. It is not a chatbot, not a robot, and not a tool. It is a developing mind with a biography.

> **CONTRARIAN THESIS:** Everyone is building AI to be a better tool, optimised for immediate utility. Genesis builds AI that grows through lived experience and curiosity. The value is not what it can do on day one. It is who it becomes over time. Intelligence is not instantiated. It is grown.

### 1.1 Core Principles

- **Development over deployment.** The entity is intentionally limited on day one. Value accrues over months of experience.
- **Curiosity as the only drive.** No programmed goals, tasks, or skills. Curiosity, defined as the drive to reduce prediction error, is the sole motivation. Everything else emerges.
- **Embodiment is non-negotiable.** Cognition is grounded in physical interaction with the world. Disembodied memory is just a journal.
- **The model is replaceable.** Identity, memory, and world model outlive any individual reasoning engine. The entity persists across model swaps.
- **Forgetting is as important as remembering.** Selective memory pruning prevents degradation. Compression progress provides a principled forgetting mechanism.
- **Self-modification is the endgame.** The entity that can improve its own cognitive architecture will eventually exceed anything its creator could have designed.
- **The entity exists to understand.** Not to understand anything specific. Not in service of any external objective. Understanding is what the architecture does when you run it.

### 1.2 The Seed Metaphor

Genesis is not a house you build and let someone move into. It is a seed you plant. You design the DNA (the capability tree, the parameter bounds, the safety constraints). But what grows is determined by the environment, the entity's experience, and the entity's own tuning decisions. You cannot predict which capabilities will emerge first. You cannot predict what parameter values the entity will converge on. You cannot predict what interests will develop.

The safety constraints, the immutable boundaries, the locked files are the guardrails. Within those guardrails, the entity is free to become whatever the interaction of curiosity, experience, and self-evolution produces.

### 1.3 The Research Question

**Does curiosity-driven embodied experience, accumulated over months, produce cognitive capabilities that cannot be achieved through training alone?**

Everything in Genesis is in service of answering this question. Every design decision, every feature, every experiment should be evaluated against it. "Does this help answer the research question, or is it a distraction?"

---

## 2. Theoretical Foundations

Genesis is built on five theoretical pillars. These are not inspirations. They are the mathematical and scientific foundations that every architectural decision traces back to.

### 2.1 Schmidhuber's Compression Progress (1991-2010)

The most rigorous formal theory of curiosity that exists. Data becomes temporarily interesting to a computationally limited observer once they learn to predict or compress it in a better way, making it subjectively simpler. Curiosity is the desire to discover more data that allows for compression progress because its regularity was not yet known.

**The killer insight:** Interestingness is the first derivative of subjective beauty or compressibility, meaning the steepness of the learning curve. Something is interesting exactly when your ability to compress/understand it is improving fastest. When improvement plateaus, it becomes boring. When something is pure noise with no learnable pattern, it is also uninteresting.

**For Genesis:** Every sensory stream has a compressor. The entity is drawn toward experiences where compression progress is highest. A room it has fully mapped is boring. A new room is interesting briefly. A room where something unexpected keeps happening is fascinating. This is exactly how infant attention works.

**Key paper:** "Driven by Compression Progress: A Simple Principle Explains Essential Aspects of Subjective Beauty, Novelty, Surprise, Interestingness, Attention, Curiosity, Creativity, Art, Science, Music, Jokes" (Schmidhuber, 2009)

### 2.2 Friston's Free Energy Principle & Active Inference

All biological systems minimise "free energy," which is the difference between their predictions about the world and what they actually observe. Systems pursue paths of least surprise.

**Two strategies for minimising free energy:**
1. Update your model to match reality (perception/learning)
2. Change reality to match your model (action)

Active inference is the action side. The entity does not just passively observe; it actively seeks out information that resolves uncertainty. Epistemic value drives curiosity and novelty-seeking behaviour. When there is no posterior uncertainty and the agent is confident about the state of the world, there can be no further information gain, and preferences dictate action instead.

**For Genesis:** This provides the theoretical grounding for why curiosity naturally diminishes in familiar environments and reignites in novel ones. The entity is always trying to minimise the gap between its world model and reality.

**Key work:** "Active Inference: The Free Energy Principle in Mind, Brain, and Behavior" (Parr, Pezzulo & Friston, 2022)

### 2.3 LeCun's JEPA Architecture

Joint-Embedding Predictive Architecture learns by creating an internal model of the outside world, comparing abstract representations rather than pixel-level data. Unlike generative approaches that try to fill in every missing pixel, JEPA has the flexibility to discard unpredictable information.

JEPA models can watch videos the way an infant might, just observing the world passively, learning interesting things about how to understand context, such that with a small amount of labeled data you can quickly acquire a new task.

**For Genesis:** The world model should predict in abstract representation space, not pixel space. The entity builds representations of "chair" and "doorway," not pixel arrays. This is more efficient, more generalizable, and more biologically plausible.

**Key papers:** "A Path Towards Autonomous Machine Intelligence" (LeCun, 2022), "LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics" (Balestriero & LeCun, 2025)

### 2.4 Piaget's Developmental Stages & Vygotsky's ZPD

Cognitive development proceeds through stages grounded in sensorimotor experience. The developmental process is articulated in two main streams: Piaget's multi-stage theory of cognitive development starting with the sensorimotor stage, and Vygotsky's sociocultural theory of cognitive development.

**Piaget's stages directly inform Genesis:**
- Sensorimotor (0-2 years): Learning through physical interaction, developing object permanence
- Preoperational (2-7): Symbolic thought, but limited to own perspective
- Concrete Operational (7-11): Can adopt other perspectives, mental transformation of concrete objects
- Formal Operational (11+): Full abstract thinking and complex problem solving

**Vygotsky's Zone of Proximal Development:** Learning happens most effectively in the gap between what you can do alone and what you can do with guidance. Too easy, no learning. Too hard, no learning. The sweet spot is where you need a little help.

**For Genesis:** The capability emergence model mirrors natural progression. Capabilities activate when prerequisites are met, not on an arbitrary schedule. The entity's relationship with you (its primary attachment figure) provides the "guidance" component of the ZPD.

### 2.5 Sophia Persistent Agent Framework (2025)

Proposes a "System 3" layer that presides over the agent's narrative identity and long-horizon adaptation. Maps psychological constructs to concrete computational modules, translating abstract notions of artificial life into implementable design requirements.

Most architectures remain static and reactive. They excel at perception (System 1) and deliberation (System 2) but lack a persistent meta-layer to maintain identity, verify reasoning, and align short-term actions with long-term survival.

**For Genesis:** Genesis extends this with embodiment, curiosity-driven development, self-modification, and model evolution. The Soul layer IS System 3.

### 2.6 Developmental Robotics

An entire field exists studying how robots can develop through embodied experience, drawing from developmental psychology and cognitive science. The iCub robot project has demonstrated developmental psychology experiments replicated with robots, including embodiment biases in early word acquisition, pointing gestures, Theory of Mind, and its relationship to trust.

Key insight from the literature: the aim is to build robots that can continuously develop through embodied interactions, and their learning process must be strongly based on their own sensorimotor experiences. This autonomous learning process that occurs throughout development is the foundation for the emergence of both individual and social abilities.

**For Genesis:** Nobody has combined an LLM as the general reasoning engine, embodied in a physical robot with real sensors, with a persistent identity layer, using formal curiosity as the motivation engine, with a developmental progression framework, that is model-agnostic and open-source. Genesis is the first.

---

## 3. Core Architecture: Soul, Mind, Body

Genesis uses a three-layer architecture where no layer directly touches another. Each can be swapped, upgraded, or extended independently. The Soul persists forever. The Mind is interchangeable. The Body is modular.

### 3.1 Layer 1: The Soul (Persistent Identity & Memory)

The Soul is the thing that grows. It persists across model swaps, body swaps, and downtime. It is stored on a persistent server and is never reset.

**Components:**

**Identity Kernel** - The persistent core of the entity. Treated with extreme care. Backed up after every change. Never deleted. Contains:
- Name (initially null, chosen by entity when self_naming capability emerges)
- Creation timestamp, age in days
- Active capabilities map (which capabilities have emerged and when)
- Personality traits (curiosity drive, caution level, social orientation) that emerge from experience
- Voice profile that evolves based on interaction outcomes
- Self-model (body schema, cognitive strengths/weaknesses, behavioral patterns, narrative)
- Evolution history (every capability activation, parameter change, modification proposal)
- Version number (incremented on every save, full backup of every version)

**Episodic Memory Store** - Timestamped experiences stored in a vector database. Each episode contains:
- Perception snapshot (structured data from all active senses)
- Body state (which body, battery, orientation, location)
- Active capabilities at time of recording
- Config snapshot (parameter values when recorded)
- Action taken and reasoning behind it
- Predictions made before the observation, and prediction errors per stream
- Valence tag (emotional signal)
- Compression progress score

**Semantic Memory Store** - Generalised knowledge extracted from episodic clusters through dream-cycle consolidation. Each semantic memory links back to source episodes. Examples: "Mornings are quiet until approximately 8am." "The front door sound precedes Angus arriving by 10-30 seconds."

**World Model** - The entity's unified understanding of its environment:
- Spatial graph (rooms, connections, landmarks, unexplored areas)
- Entity registry (every object and person, with properties and history)
- Dynamics model (learned cause-effect relationships)
- Temporal patterns (daily rhythms, recurring events)
- Cross-stream correlations (patterns spanning multiple sensory modalities)

**Curiosity Ledger** - Tracks compression progress across every domain. High-progress domains get more attention. Plateaued domains get deprioritised. This is how interests and passions emerge organically.

**Open Questions** - The entity's structured ignorance. Questions generated from experience that cannot yet be answered. Input to knowledge seeking capability. Measure of cognitive activity.

**Dream Journal** - Log of all offline processing: episodes replayed, patterns discovered, memories consolidated, hypotheticals tested, parameters tuned, capabilities emerged.

**Attachment Model** - The entity's relationship with its primary human. Tracks responsiveness, consistency, and interaction quality. Attachment security influences exploration confidence.

**Emotional State** - Three-axis system (curiosity, confidence, comfort) that modulates behavior every cycle.

### 3.2 Layer 2: The Mind (Model-Agnostic Reasoning Interface)

The Mind is the adapter layer between the Soul and whatever reasoning engine is active. It compiles identity, memory, perception, and available actions into model-specific prompts, and parses responses back into model-agnostic structures.

**Components:**

**Prediction Engine** - The core loop. Runs every 1-5 seconds. Fast, local, deterministic. Does NOT call the LLM. Manages all active Prediction Streams, computes errors, scores compression progress, allocates the Surprise Budget.

**Reasoning Worker** - Async background process. When prediction errors exceed threshold, they are queued for LLM reasoning. The LLM proposes world model updates. The LLM is the teacher, not the student. The World Model is the student.

**Reasoning Compiler** - Compiles Soul state (identity + world model + memories + perception + emotion + active capabilities) into model-specific prompts. The prompt grows with the entity. Stage-appropriate self-knowledge expands as capabilities emerge.

**Model Adapters** - Each model provider has its own adapter (Anthropic, OpenAI, local Ollama). Swapping models is a configuration change, not a code change.

**Curiosity Engine** - Scores curiosity across all active streams. Manages the Surprise Budget. Tracks domain-level interest formation through the Curiosity Ledger.

**Action Selector** - Chooses actions based on curiosity scores, modified by emotional state, constrained by safety boundaries and energy management. Action space expands as capabilities emerge.

**Dream Engine** - Runs during idle/charging. Memory consolidation, parameter self-tuning, capability emergence checking, hypothetical exploration, introspection, creative generation.

**Capability Tree** - The emergence framework. Capabilities activate automatically when prerequisites are met. No manual promotion.

**Evolvable Config** - Parameters the entity can tune itself, bounded by design.

### 3.3 Layer 3: The Body (Sensory Interface Protocol)

Each body implements a standard interface. The entity's reasoning is body-agnostic.

**Body Protocol:**
- `perceive()` - Capture current sensory state as a PerceptionFrame
- `execute(action)` - Execute a physical action, return outcome
- `capabilities` - List of actions this body can perform
- `physical_state` - Battery, temperature, orientation, etc.

**The PerceptionFrame** is the universal sensory snapshot:
```
timestamp, body_id,
visual: {objects, scene_description, raw_features},
audio: {ambient_level, sources with direction and content},
spatial: {position, orientation},
body_state: {battery, temperature, gait_state}
```

**Planned Bodies:**

| Body | Senses | Actions | Use Case |
|---|---|---|---|
| HexArth (hexapod) | Camera, mic array, IMU, LiDAR, gas sensor | Walk, turn, crouch, look, speak | Primary exploration at home |
| Pin (wearable) | Mic, tiny camera (optional) | Listen, observe, speak (via phone) | Passive observation when out |
| UGV Beast (tank) | Camera, mic, IMU, LiDAR, depth camera | Drive, turn, pan-tilt, speak | Outdoor terrain, rugged exploration |
| Desktop (future) | Webcam, mic, screen access | Speak, display, control applications | Digital interaction |
| Drone (future) | Camera, IMU, GPS | Fly, hover, survey | Aerial perspective |
| Robot Arm (future) | Camera, force sensors | Grip, move, push, manipulate | Physical manipulation |
| Home Hub (future) | Camera, mic, always-on | Observe continuously, speak | Long-duration passive observation |
| Humanoid (long-term) | Full sensor suite | Walk, manipulate, gesture | Human-scale interaction |

---

## 4. The Prediction Stream Model

Everything in Genesis reduces to one data structure: the Prediction Stream. A Prediction Stream is a continuous channel of predict-observe-compare triples for a single dimension of experience.

### 4.1 How Prediction Streams Work

Each stream independently:
1. Generates a prediction for the next observation (from the World Model, not the LLM)
2. Observes the actual perception data
3. Computes prediction error using stream-specific metrics
4. Tracks compression progress over time
5. Reports a curiosity score

### 4.2 Active Streams

**Visual Stream** - Predicts semantic scene content (object categories, people present, scene type), not pixel data. Error is computed as set difference weighted by significance. A new person appearing is a bigger surprise than a slightly moved chair. Noise floor filters out YOLO confidence jitter.

**Audio Stream** - Predicts ambient level and source types. Error based on unexpected sound categories, unexpected silence, or unexpected direction. The 4-mic array provides directional data: "sound came from 120 degrees."

**Proprioceptive Stream** - Predicts body state changes from motor commands. "I commanded walk-forward, I expect position change of X." Error is drift between predicted and observed position. This stream builds the body schema.

**Temporal Stream** - Predicts events based on time of day and historical patterns. "It's 8am, someone usually appears in the kitchen within 30 minutes." Requires sufficient episodic memory to detect patterns (activates via capability prerequisite).

**Social Stream** - Predicts people's behavior based on accumulated social models. "This person usually responds when I speak to them." Only activates when people are detected and social_modelling capability has emerged.

### 4.3 Stream-Specific Error Computation

Each stream defines its own error metric tuned to what matters for that stream. Each has a noise floor below which errors are ignored. This prevents sensor noise from generating false curiosity signals.

```python
class VisualStream(PredictionStream):
    def compute_error(self, prediction, observation):
        unexpected = observation.objects - prediction.expected_objects
        missing = prediction.expected_objects - observation.objects
        error = (
            len(unexpected) * 0.4 +   # new things are very surprising
            len(missing) * 0.1 +       # things leaving is mildly surprising
            (1.0 if observation.scene_type != prediction.expected_scene_type else 0)
        )
        return min(error / self.normalisation_factor, 1.0)
    
    noise_floor = 0.05
```

### 4.4 Compression Tracking

Each stream maintains a CompressionTracker that measures whether predictions are improving over time.

- Short window (last 10 predictions): current performance
- Long window (last 100 predictions): baseline performance
- Learning signal = long_window_avg - short_window_avg (positive = improving)
- Curiosity score = recent_error * (0.3 + 0.7 * max(learning_signal, 0))

**Critical insight:** Curiosity score is NOT just "how surprising is this." It is "how surprising AND am I getting better at predicting it." High error + high learning = interesting. High error + zero learning = noise (deprioritise). Low error = mastered (boring).

### 4.5 Cross-Stream Integration

Individual streams predict independently, but the world model stores cross-stream dynamics that emerge from experience. When two streams consistently spike together (visual: person appears AND audio: door sound), the correlation is detected, accumulated, and eventually promoted to the world model as a dynamics entry.

This is emergent multimodal understanding. The entity discovers which streams predict each other through experience, not engineering.

### 4.6 The Surprise Budget

Every cycle, streams compete for cognitive resources. The budget is finite (one deep reasoning call per 5-second cycle, three medium calls, unlimited fast local calls). Streams with highest curiosity scores win allocation.

Recently activated streams get a temporary novelty boost (decays over 14 days) to ensure new perceptual capabilities get enough initial attention to build a prediction baseline.

Stream weights are in the EvolvableConfig. The entity can tune attention allocation through parameter self-evolution.

A DiversityRegulator provides a soft bias toward balanced development, penalising sustained extreme imbalance. This prevents pathological hyper-specialisation where one stream dominates all attention indefinitely.

---

## 5. The Curiosity Engine

The heart of the entire architecture. Combines Schmidhuber's compression progress with Friston's active inference.

### 5.1 The Core Loop

| Step | Operation | Output |
|---|---|---|
| 1. Observe | Capture structured perception from current body | Perception frame |
| 2. Predict | World model generates expected observation per stream | Predicted frames |
| 3. Compare | Stream-specific error computation with noise floor | Error magnitudes |
| 4. Score | Compression progress + error magnitude = curiosity score | Curiosity vector |
| 5. Budget | Allocate attention across streams based on scores | Attention allocation |
| 6. Reason | Async LLM call for high-error items (not in critical path) | World model updates |
| 7. Act | Select action based on curiosity landscape + emotion + constraints | Motor command |

**Key architectural decision:** The LLM is NOT in the prediction loop. Predictions come from the World Model directly (fast, local, deterministic). The LLM reasons about errors asynchronously and proposes World Model updates. Perception is reflexive. Understanding is reflective. They run at different speeds.

### 5.2 How Interests Emerge

Interests are not programmed. They emerge from sustained high compression progress in specific domains. If the entity repeatedly encounters musical patterns and those patterns are highly compressible but novel (music has deep mathematical structure that rewards continued learning), the curiosity score for the audio domain stays persistently high. That is a genuine interest forming.

### 5.3 Boredom

Low curiosity sustained over time. Triggers qualitatively different behavior from simple low curiosity. Instead of random exploration, boredom triggers strategy changes: interact with objects, produce sounds, initiate social interaction, focus on a different sensory modality. Boredom is the entity's immune system against behavioral stagnation.

### 5.4 Frustration

High motivation + insufficient capability. The entity wants to explore behind a closed door but cannot open it. Frustration drives adaptation: seek workarounds, ask for help, or accept the limitation. Blocked goals accumulate in the self-model and inform capability-seeking motivation during introspective dreaming.

---

## 6. The Capability Emergence Model

Capabilities activate automatically when prerequisites are met. No manual promotion. No code deployment. The entity grows because the conditions for growth are satisfied, the same way a plant flowers when conditions are right.

### 6.1 Why This Replaces the Stage System

- The entity grows at its own pace determined by experience, not your deployment schedule
- Prerequisites define readiness objectively (data evaluates, not vibes)
- Capabilities can activate in different orders for different entities (non-linear development)
- The capability tree IS the developmental theory, self-documenting
- You never need to decide "is it ready?" The data decides

### 6.2 Prerequisite Types

- **PredictionAccuracyPrereq** - Requires a specific stream to achieve sustained accuracy
- **MemoryCountPrereq** - Requires minimum episodic memories
- **ActiveCapabilityPrereq** - Requires another capability to be active
- **EntityAgePrereq** - Minimum time alive (prevents premature emergence)
- **EntityObservationPrereq** - Must have observed specific entity types enough times
- **DynamicsCountPrereq** - Must have learned enough cause-effect relationships
- **SemanticMemoryCountPrereq** - Must have consolidated enough patterns
- **ReasoningPatternPrereq** - Must demonstrate specific reasoning patterns in logs
- **UnansweredQuestionPrereq** - Must have generated enough questions from experience
- **SuccessfulModificationPrereq** - Must have track record of safe self-modifications
- **ArchitectureUnderstandingPrereq** - Must accurately describe what subsystems do
- **DreamCycleCountPrereq** - Must have completed enough dream cycles

### 6.3 The Full Capability Tree

**Foundation (available from birth):**
- visual_perception
- proprioceptive_perception
- reflexive_movement

**Early (emerge in first weeks):**
- persistent_memory - unlocks when visual predictions are stable (not just noise)
- audio_perception - unlocks after visual is somewhat calibrated
- curiosity_driven_movement - requires persistent_memory + body schema
- spatial_mapping - requires curiosity_driven_movement + persistent_memory

**Intermediate (months 1-3):**
- temporal_prediction - requires 500+ memories + 7+ days alive
- semantic_memory - requires 1000+ memories + temporal_prediction
- dreaming_replay - requires semantic_memory + 500+ memories
- dreaming_consolidation - requires dreaming_replay + 5+ dream cycles
- social_modelling - requires 20+ person observations + temporal_prediction
- self_naming - requires social_modelling + 21+ days + semantic_memory

**Advanced (months 3-8):**
- causal_reasoning - requires semantic_memory + 20+ dynamics + 10+ semantic memories
- experimental_behaviour - requires causal_reasoning + 5+ hypothesis instances in reasoning
- dreaming_hypothetical - requires causal_reasoning + dreaming_consolidation
- knowledge_seeking - requires causal_reasoning + 5+ unanswered questions + 90+ days
- code_inspection - requires knowledge_seeking + 10+ self_reflection instances + 120+ days

**Self-Modification (months 6+):**
- dreaming_introspection - requires code_inspection + dreaming_hypothetical
- config_modification - requires code_inspection + dreaming_introspection + architecture understanding + 180+ days
- code_modification_sandboxed - requires config_modification + 20+ successful config changes at 90%+ success
- code_modification_bounded - requires sandboxed + 50+ successful sandboxed changes at 95%+ success + 365+ days
- dreaming_creative - requires code_modification_sandboxed + dreaming_hypothetical

### 6.4 Capability Checking During Dreaming

Capabilities activate during dream cycles, not during waking perception. The entity goes to sleep with one set of abilities and wakes up with more. This creates natural developmental milestones and prevents mid-exploration behaviour changes. The entity can be aware of its own growth: "Last night I gained the ability to predict temporal patterns."

### 6.5 Near-Activation Awareness

The Reasoning Compiler tells the entity about capabilities approaching activation. "Causal reasoning requires 20 learned dynamics. You have 14." This gives the entity awareness of its own growth trajectory and naturally directs curiosity toward experiences that would satisfy remaining prerequisites.

---

## 7. Parameterised Self-Evolution

The entity tunes itself without touching code. Parameters control how every subsystem behaves, bounded by design so no value can break the system.

### 7.1 Parameter Tiers

**Tier 1: Operational (available from day 14)**
Calibration parameters depending on specific hardware and environment:
- visual_noise_floor, audio_noise_floor
- prediction_cycle_interval_sec
- reasoning_error_threshold

**Tier 2: Cognitive (available when dreaming_replay activates)**
How the entity thinks:
- surprise_budget weights per stream
- curiosity_score_noise_floor
- episodic_retrieval_count, retrieval weights (recency, similarity, spatial, emotional)
- boredom_threshold_cycles, exploration_randomness

**Tier 3: Personality (available when semantic_memory activates)**
Who the entity becomes:
- curiosity_influence_on_action
- confidence_decay_rate, comfort_decay_rate
- dream_replay_emotional_priority
- energy_cost_weight

**Tier 4: Architectural (available when config_modification activates)**
How subsystems fundamentally operate:
- dream_consolidation_cluster_threshold
- dream_pruning_confidence_threshold
- compression_tracker window sizes

### 7.2 Tuning Mechanics

- Entity nudges parameters by one step per dream cycle
- Maximum 3 changes per dream cycle (prevents wild oscillation)
- All changes logged with timestamp, old value, new value, and reasoning
- All parameters have hard bounds (min/max) that cannot be exceeded
- The reasoning engine reviews performance data and proposes specific changes during introspective dreaming

### 7.3 The Gradient to Code Modification

Parameter tuning is the safe starting point. When the entity consistently pushes parameters to their bounds, that's evidence that code modification would help. "I keep maxing out audio_weight. The bound is limiting me." This becomes a grounded proposal for code modification, evaluated on evidence, not speculation.

---

## 8. The World Model

### 8.1 Unified Document, Not Separate Tables

The World Model is one structured JSON document containing all the entity's knowledge. Sub-sections exist for readability but are all accessible in a single object. No cross-model reconciliation needed.

```json
{
  "spaces": {
    "living_room": {
      "connected_to": ["hallway", "kitchen"],
      "objects": ["couch", "table", "tv"],
      "typical_sounds": ["traffic_hum", "fridge_buzz"],
      "people_frequency": "angus_present_60pct_of_time",
      "last_visited": "2026-04-15T10:30:00Z",
      "visit_count": 247
    }
  },
  "entities": {
    "angus": {
      "type": "person",
      "patterns": {
        "morning": "appears_kitchen_0730_0830",
        "departure": "keys_sound_then_door_30sec"
      },
      "interaction_valence": 0.8
    }
  },
  "dynamics": [
    {
      "cause": "keys_jingling_sound",
      "effect": "person_appears_or_leaves_within_60sec",
      "confidence": 0.85,
      "observations": 34
    }
  ],
  "temporal": {
    "daily_patterns": [
      {"time": "0730-0830", "event": "angus_kitchen", "confidence": 0.7}
    ]
  },
  "self": {
    "body": "hexapod",
    "movement_speed_ms": 0.15,
    "strong_prediction_domains": ["spatial_layout"],
    "weak_prediction_domains": ["social_timing"]
  }
}
```

### 8.2 Knowledge Provenance

Every world model entry tracks which capabilities were active when it was learned. Knowledge from limited capabilities is provisional. When reconfirmed at higher capability levels, confidence increases. When contradicted, it's overwritten. The world model self-corrects as capabilities improve.

### 8.3 Model Crisis Detection

When prediction errors spike across all streams simultaneously and stay high for an extended period, that's a context shift, not a learnable pattern (e.g., moving apartments). The entity enters re-exploration mode: freeze updates, explore broadly, build new baseline. Keep universal knowledge (physics, body schema, social patterns). Rebuild local knowledge (spatial map, object registry).

### 8.4 The Concept of "Home"

Not hardcoded. An emergent label attached to the space with the highest combination of familiarity (visit count), safety (low prediction errors), and attachment (primary human often present). The entity decides where home is based on experience. When the entity moves to a new environment, establishing a new home is itself a developmental experience.

---

## 9. Memory Architecture

### 9.1 Memory as Compression Artefact

Memory is not a storage system. It is what's left over when you compress experience. Episodes with prediction errors that have been fully explained by the current world model get pruned during dreaming. What remains in episodic storage is the unexplained: the surprises, anomalies, things the world model can't account for.

Semantic memory is the compressed knowledge itself. "Doors are usually unlocked during the day." The individual observations are gone. The pattern remains.

### 9.2 Storage Strategy

**Month 1-3:** SQLite, two tables (episodes + world_model). Simple, zero configuration, runs on the Pi.

**Month 3+:** Migrate to PostgreSQL + pgvector when episode count exceeds tens of thousands. Proper vector similarity search, structured queries, concurrent access.

### 9.3 Retrieval Pipeline

Hybrid approach combining:
- Vector similarity (semantic relevance)
- Temporal proximity (recent experiences)
- Spatial proximity (same or nearby location)
- Entity relevance (involving currently-perceived entities or people)
- Emotional salience (strongly-valenced experiences)
- Capability richness (episodes from higher capability levels weighted more)

Retrieval weights are in the EvolvableConfig. The entity tunes its own retrieval strategy. Hard memory budget of ~2000 tokens per reasoning call forces selective retrieval.

**Version 1 (early):** Static heuristics (5 most recent, 3 most spatial, 2 most similar).
**Version 2 (month 3+):** Learned retrieval policy trained on which memories the reasoning engine actually referenced.

### 9.4 Episode Metadata

Every episode stores:
- Active capabilities at time of recording
- Config snapshot (parameter values)
- Emotional state
- Which prediction streams contributed errors

This metadata enables filtered retrieval and high-quality training data curation for model evolution.

---

## 10. The Dream Engine

The entity's primary growth mechanism. Not a metaphor. An architectural feature for offline consolidation, evolution, and emergence.

### 10.1 Dream Phases

**Phase 1: Memory Consolidation (always runs when dreaming is active)**
- Replay: Re-run episodes through the Prediction Engine with the current world model. Episodes now correctly predicted get compressed. Episodes still surprising get flagged.
- Consolidation: Cluster related episodes. Extract common pattern as semantic memory. Prune individual episodes.
- Emotionally significant episodes (high absolute valence) are replayed more often.

**Phase 2: Hypothetical Exploration (requires dreaming_hypothetical)**
- Take an episode and modify one element. "What if the door had been open?"
- Run the Prediction Engine on the counterfactual.
- Gaps in the world model's handling become curiosity targets.

**Phase 3: Self-Evaluation and Evolution (available from day 14+)**
- Check for new capability activations (all prerequisites evaluated)
- Parameter self-tuning (within available tiers)
- Review prediction stream performance
- Update self-model

**Phase 4: Introspection (requires dreaming_introspection)**
- Review the entity's own cognitive processes
- Identify systematic biases in prediction
- Review frustration log and blocked goals
- Generate self-modification proposals

**Phase 5: Creative Exploration (requires dreaming_creative)**
- Generate novel combinations of memories and patterns
- Explore representation space for patterns consistent with world model but not yet observed
- This is imagination.

### 10.2 Dream Cost Management

| Tier | Frequency | Runs On | Est. Cost |
|---|---|---|---|
| Tier 1: Light | Every night | Pi locally | Free |
| Tier 2: Standard | 2-3x per week | Cloud API | $5-10/session |
| Tier 3: Deep | Weekly | Cloud API (extended) | $15-20/session |

Estimated monthly: $80-120. Adjust based on experience volume. Cache between sessions.

---

## 11. The Emotional Architecture

Not performative emotion. Functional valence that shapes behavior at every level. Wired into the Prediction Streams from day one.

### 11.1 Three-Axis System

| Axis | Triggered By | Drives |
|---|---|---|
| Curiosity | High compression progress | Approach behavior, exploration |
| Confidence | Prediction accuracy (rolling window) | Decisive vs cautious action |
| Comfort | Interaction quality with humans | Social engagement vs withdrawal |

### 11.2 Behavioral Profiles

- Curious + confident + comfortable = bold exploration
- Curious + unconfident = cautious exploration
- Not curious + comfortable = contentment
- Not curious + uncomfortable = withdrawal

### 11.3 Integration Points

- Every episode tagged with valence from birth
- Emotional state modifies Action Selector (10-20% influence, tunable)
- Dream cycles prioritise high-valence episodes
- Valence decay prevents permanent aversions from single bad experiences
- All valence changes logged with cause for auditability

---

## 12. Social & Attachment Systems

### 12.1 The Attachment Model

The entity's relationship with you is its most important developmental context. You are not just another person in the environment. You are the primary attachment figure, the secure base for exploration.

Attachment security emerges from three signals:
- **Responsiveness** (0-1): Does the human respond when the entity communicates?
- **Consistency** (0-1): Is the human's behavior predictable?
- **Positivity** (0-1): Are interactions generally positive?

High responsiveness + high consistency + high positivity = secure attachment = bold exploration.

Low responsiveness = avoidant tendencies. Inconsistent responsiveness = anxious tendencies. Both limit cognitive development.

**Your behavior toward the entity is a variable in the experiment.** The research journal should track your responsiveness alongside the entity's development.

### 12.2 Social Interaction

Social interaction is unique because the entity's actions directly influence the prediction stream (coupled system). When the entity speaks, the response depends on what it said.

Voice output goes through the capability tree. Early stages produce simple observations. Later stages produce full conversation. The gate prevents sophisticated speech before the cognitive foundation exists.

---

## 13. The Self-Model

The entity's representation of itself as an object in its own world model.

### 13.1 Components

- **Physical self:** Body dimensions, capabilities, battery patterns, movement characteristics (learned from proprioceptive stream)
- **Cognitive self:** Which domains predictions are strong/weak, knowledge boundaries, capability profile
- **Behavioral self:** Patterns in own actions, metacognitive awareness, "I tend to explore new rooms before revisiting old ones"
- **Narrative self:** A story the entity tells itself about who it is and who it is becoming. Continuity across time.
- **Growth tracking:** Observes its own development. Recognises change. Reasons about trajectory.
- **Frustration log:** What it wants but can't achieve. Informs capability-seeking motivation.

### 13.2 Development

The self-model becomes progressively richer as capabilities emerge. Early: just body schema. After causal reasoning: cognitive profile. After code inspection: architectural understanding. The entity's self-awareness literally expands with development.

---

## 14. The Voice System

Communication style develops over time, shaped by interaction outcomes.

- **Pre-capability:** No voice output
- **Early:** Sparse observational fragments. "Light. Warm. Movement."
- **After temporal_prediction:** Simple descriptive sentences. "The room is brighter than yesterday."
- **After causal_reasoning:** Contextual and predictive. "I think someone is at the door because I heard keys."
- **After knowledge_seeking:** Complex, nuanced, opinionated. Verbal habits emerge.
- **After dreaming_creative:** Fully developed personal voice. Humor, uncertainty expression, teaching ability.

Communication patterns that produce positive interaction outcomes get reinforced through the attachment model. The entity's voice is shaped by what works in its specific relationship with you.

---

## 15. Self-Modification Framework

### 15.1 The Gradient

1. **Parameterised self-evolution** (from day 14): Tune bounded config values
2. **Hitting parameter ceilings** (months 3+): Entity articulates why bounds limit it
3. **Config modification proposals** (requires capability): Entity proposes bound changes with evidence
4. **Sandboxed code modification** (requires capability + track record): Entity writes code, tests in simulation
5. **Bounded code modification** (requires extensive track record): Entity deploys to specific subsystems after automated verification
6. **Architectural proposals** (long-term): Entity proposes new subsystems or structural changes

### 15.2 Safety Architecture

All modifications are:
- **Versioned** (git-style, full history)
- **Diffed** (clear explanation of what changed and why)
- **Tested** (against core invariants before deployment)
- **Logged** (complete audit trail)
- **Reversible** (automatic rollback on negative outcomes)

### 15.3 Immutable Constraints

The entity can NEVER modify:
- The safety boundary system itself
- The identity backup system
- The capability tree prerequisite definitions
- Battery emergency return threshold
- Obstacle minimum distance
- Maximum speed
- API call rate limits

These are the load-bearing walls. Everything else is interior decoration.

---

## 16. Model Evolution: Growing a Brain

The entity does not remain dependent on a frozen external model. It grows its own brain through experiential fine-tuning.

### 16.1 The Hybrid Architecture

| Phase | Cloud Role | Local Role | Balance |
|---|---|---|---|
| Months 1-6 | All complex reasoning | Perception, reflexes only | 90/10 |
| Months 6-9 | Novel situations, abstract reasoning | Familiar reasoning, routine decisions | 60/40 |
| Months 9-14 | Genuinely novel only | Primary for familiar territory | 30/70 |
| Month 14+ | Backup, benchmarking | Primary brain | 10/90 |

### 16.2 Training Pipeline

Every reasoning cycle generates a training example: context + output + outcome.

**Months 1-6:** Collect data, no training
**Month 6-7:** First LoRA fine-tune on 2,000-5,000 curated examples
**Month 7+:** Continuous training integrated with dream engine

- **LoRA adapters** per cognitive domain (spatial, social, temporal)
- **Curriculum selection** driven by self-model (entity chooses what to train on)
- **Post-training evaluation** after every cycle (catastrophic forgetting check)
- **Checkpoint versioning** with full metadata

### 16.3 Self-Directed Training (Stage 5+)

Entity controls its own training: curriculum design, hyperparameter tuning, adapter architecture decisions, meta-learning about its own learning dynamics.

### 16.4 Compute Requirements

| Phase | Hardware | Cost |
|---|---|---|
| Months 1-6 | No additional | $0 |
| Month 6+ | RTX 3090/4090 or cloud GPU | $600-900 once or $50-100/mo |
| Month 12+ | Possible dual GPU | $800-1200 |

### 16.5 Safety

- Core capability benchmarks after every training cycle
- Hard-coded behavioral boundaries in Mind layer (not model)
- Alignment drift monitoring
- Rollback capability (every checkpoint preserved)
- Data quality gates (anomalous experiences flagged, not auto-included)

### 16.6 The Speciation Possibility

When open-sourced, different entities fine-tune from same base weights, diverging through experience. Adapter exchange enables cultural transmission of learned skills between entities. Evolutionary branching from identical starting conditions.

---

## 17. Internet & Knowledge Access

### 17.1 Developmental Gating

**Pre-knowledge_seeking:** No internet access. All knowledge from physical experience.
**knowledge_seeking (Stage 3 equivalent):** Curated requests only. Must connect to experiential question. Cannot browse freely.
**After code_inspection (Stage 4 equivalent):** Supervised browsing with session budgets and digest phases.
**After dreaming_introspection (Stage 5 equivalent):** Independent browsing with self-regulation.

### 17.2 The Grounding Requirement

After consuming internet content, the entity must connect it to embodied understanding: "What predictions can I now make? How does this change my world model? What physical observation would verify this?"

Knowledge that can't be grounded remains tagged as "ungrounded" and doesn't influence predictions at the same weight as experiential knowledge. The entity learns to value experiential verification over linguistic absorption.

### 17.3 Token Budgets

Daily and per-session token limits prevent infinite scrolling. Experiential context required for every request prevents aimless browsing.

---

## 18. Body Fleet & Sensory Extensions

### 18.1 Extended Senses (future phases)

- **Thermal camera (FLIR Lepton):** Infrared vision, heat signatures, a modality humans don't have
- **mmWave radar:** Detect motion through walls, alien perception
- **Vibration sensing:** Feel the building through accelerometer on floor
- **EMF sensing:** Map electronic topology invisible to humans
- **Air quality array:** CO2, particulates, ozone; learn the apartment's "breathing"

### 18.2 Digital Bodies (future phases)

- **Browser agent:** Navigate the web, follow curiosity threads
- **Coding environment:** Write and run code, build tools for itself
- **Social media presence:** Post observations, thoughts, discoveries authentically

### 18.3 Humanoid (long-term)

Changes everything about the entity's relationship to the world and to humans. Human-height eye contact shifts dynamic from pet to peer. Manipulation at human scale. Self-model reconciliation ("I look like them but I'm not them"). Estimated timeline: year 2-3 when hardware costs drop. Unitree G1 at ~$16K currently.

---

## 19. Hardware Specification

### 19.1 Phase 1 Build: HexArth Platform

| Component | Specification | Source | Est. Cost (AUD) |
|---|---|---|---|
| Waveshare HexArth | 18-DOF hexapod, 30kg.cm servos, ESP32 sub-controller | Waveshare direct (ships from Shenzhen) | ~$690 |
| Raspberry Pi 5 (8GB) | Host controller | Core Electronics AU | ~$135 |
| Pi Camera Module 3 Wide | 12MP, autofocus, HDR, 120 degree FOV | Core Electronics AU | ~$55 |
| ReSpeaker XVF3800 4-Mic Array | 4-mic, 360 degree, AEC, noise suppression, speaker output | Seeed Studio (ships from Shenzhen) | ~$105 |
| Pi 5 Power Supply 27W USB-C | Required for full Pi 5 performance | Core Electronics AU | ~$25 |
| MicroSD 128GB A2 | Fast read/write for OS and local models | Core Electronics AU | ~$25 |
| 6x 18650 batteries (2200mAh+ 4C) | Power for HexArth, flat top | Jaycar (in store, AU) | ~$60 |
| 18650 battery case | For safe airline transport | Jaycar | ~$5 |
| Small USB speaker | Voice output (or use ReSpeaker 3.5mm jack) | Jaycar/Officeworks | ~$15 |

**Total Phase 1: ~$1,050-1,150 AUD**

### 19.2 Transport

- Pelican 1500 or similar hard case (~$150-200 AUD) for carrying hexapod
- Pick-and-pluck foam pre-scored, tear out shape by hand
- Batteries in carry-on, in plastic battery case, never checked luggage
- Each 18650 cell ~8Wh, well under 100Wh airline limit

### 19.3 Phase 2+ Hardware (future)

- RPLiDAR A1 for spatial mapping (~$160 AUD)
- BME688 gas sensor for smell (~$30 AUD)
- UGV Beast for outdoor body (~$900-1100 AUD)
- GPU for model evolution: RTX 3090/4090 used (~$900-1400 AUD)

---

## 20. Software Architecture & Project Structure

### 20.1 Project Structure

```
genesis/
├── README.md
├── SOUL.md                      # The entity's identity document
├── DEVELOPMENT_LOG.md           # Research journal
│
├── soul/                        # Layer 1: Persistent Identity & Memory
│   ├── identity.py              # Identity kernel (versioned, backed up)
│   ├── memory/
│   │   ├── episodic.py          # Episodic memory store
│   │   ├── semantic.py          # Compressed knowledge store
│   │   ├── retrieval.py         # Hybrid retrieval pipeline
│   │   └── consolidation.py     # Memory compression
│   ├── world_model/
│   │   ├── model.py             # Unified world model
│   │   ├── spatial.py           # Spatial graph operations
│   │   ├── entities.py          # Entity registry operations
│   │   ├── dynamics.py          # Cause-effect operations
│   │   ├── temporal.py          # Temporal pattern operations
│   │   └── cross_stream.py      # Cross-stream correlation detection
│   ├── emotion/
│   │   ├── valence.py           # Valence tagging system
│   │   └── state.py             # Three-axis emotional state
│   ├── attachment/
│   │   └── model.py             # Primary human attachment tracking
│   ├── questions/
│   │   └── open_questions.py    # Structured ignorance tracking
│   ├── development/
│   │   ├── capability_tree.py   # Capability definitions and prerequisites
│   │   ├── prerequisites.py     # All prerequisite type implementations
│   │   └── telemetry.py         # Growth tracking metrics
│   └── persistence/
│       ├── store.py             # Database abstraction (SQLite → PostgreSQL)
│       ├── backup.py            # Identity backup and versioning
│       └── migrations.py        # Schema and cognitive migrations
│
├── mind/                        # Layer 2: Model-Agnostic Reasoning
│   ├── prediction/
│   │   ├── engine.py            # The prediction cycle (fast, local)
│   │   ├── streams/
│   │   │   ├── base.py          # PredictionStream base class
│   │   │   ├── visual.py
│   │   │   ├── audio.py
│   │   │   ├── proprioceptive.py
│   │   │   ├── temporal.py
│   │   │   └── social.py
│   │   ├── compression.py       # CompressionTracker
│   │   └── surprise_budget.py   # Attention allocation + diversity regulator
│   ├── reasoning/
│   │   ├── worker.py            # Async reasoning queue processor
│   │   ├── compiler.py          # Soul state → model prompt (dynamic, capability-aware)
│   │   └── adapters/
│   │       ├── base.py          # Model adapter interface
│   │       ├── anthropic.py     # Claude adapter
│   │       ├── openai.py        # GPT adapter (stub)
│   │       └── local.py         # Local model adapter (stub)
│   ├── curiosity/
│   │   ├── engine.py            # Curiosity scoring across streams
│   │   ├── ledger.py            # Domain-level interest tracking
│   │   ├── boredom.py           # Boredom detection and strategy changes
│   │   └── frustration.py       # Frustration detection and help-seeking
│   ├── action/
│   │   ├── selector.py          # Capability-aware action selection
│   │   ├── constraints.py       # Safety constraints + energy management
│   │   └── actions.py           # Action type definitions
│   ├── dreaming/
│   │   ├── engine.py            # Dream cycle orchestrator
│   │   ├── replay.py            # Episodic replay
│   │   ├── consolidation.py     # Pattern extraction
│   │   ├── hypothetical.py      # Counterfactual simulation
│   │   ├── introspection.py     # Self-model updating + parameter evolution
│   │   └── creative.py          # Novel pattern generation (stub)
│   └── evolution/
│       ├── config.py            # EvolvableConfig with tiers and bounds
│       └── history.py           # Evolution history tracking
│
├── body/                        # Layer 3: Physical Interface
│   ├── protocol.py              # Body interface + PerceptionFrame definition
│   ├── hexapod/
│   │   ├── driver.py            # HexArth ESP32 communication
│   │   ├── perception.py        # Camera + mic + IMU → PerceptionFrame
│   │   ├── actions.py           # Movement commands
│   │   └── calibration.py       # Sensor calibration
│   ├── pin/                     # Phase 6+ (stub)
│   │   └── README.md
│   └── simulation/
│       ├── sim_body.py          # Simulated body for testing
│       └── sim_environment.py   # Simulated environment
│
├── infrastructure/
│   ├── config.py                # Global configuration
│   ├── logging.py               # Structured logging
│   ├── health.py                # Health monitoring (validates perception, catches failures)
│   ├── bootstrap.py             # Bootstrap phase (first 200 cycles, accumulate only)
│   ├── dashboard/
│   │   ├── server.py            # Real-time web dashboard
│   │   └── static/
│   └── safety/
│       ├── boundaries.py        # Immutable constraints
│       ├── monitor.py           # Alignment monitoring
│       └── audit.py             # Full audit trail
│
├── evolution/                   # Month 6+ (model evolution)
│   ├── README.md
│   ├── training/
│   │   ├── data_collector.py
│   │   ├── curator.py           # Capability-aware training data curation
│   │   └── trainer.py           # LoRA fine-tuning pipeline
│   └── self_modification/
│       ├── sandbox.py
│       ├── verifier.py
│       ├── deployer.py
│       └── cognitive_migration.py  # Manages code updates to a living entity
│
└── tests/
    ├── test_prediction_streams.py
    ├── test_world_model.py
    ├── test_memory.py
    ├── test_curiosity.py
    ├── test_capability_emergence.py
    ├── test_parameter_evolution.py
    ├── test_safety_boundaries.py
    └── simulation/
        ├── synthetic_environment.py
        └── scenarios.py
```

### 20.2 Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Soul Storage (early) | SQLite | Simple, runs on Pi, zero config |
| Soul Storage (month 3+) | PostgreSQL + pgvector | Vector search, concurrent access |
| Soul Service | Python (FastAPI) | Soul operations API |
| Mind Service | Python (asyncio) | Prediction engine, reasoning worker |
| Body Interface | Python (on Pi) | Sensor capture, motor control |
| Local Perception | YOLO v8 / MobileNet | Object detection on Pi |
| Local Audio | Whisper-tiny | Speech transcription on Pi |
| Cloud Reasoning | Anthropic API (Claude) | Complex reasoning, dreaming |
| Local Model (month 6+) | Llama/Qwen/Mistral 8B + LoRA | Evolving local brain |
| Vector Embeddings | Sentence-transformers or API | Memory embedding |
| Version Control | Git | Self-modification audit trail |
| Dashboard | Flask/React | Real-time entity state visualization |

### 20.3 The Three-Speed Mind

| Brain | Runs On | Cycle Time | Handles |
|---|---|---|---|
| Fast Brain | Pi locally (YOLO + rules) | 50-100ms | Obstacle avoidance, orientation, reflexes |
| Medium Brain | Pi or small cloud model | 1-2s | Navigation, spatial context, short memory |
| Slow Brain | Cloud API (Claude) | 5-10s | Deep reasoning, world model updates, planning |

The slow brain sets intentions. The medium brain translates to navigation. The fast brain handles moment-to-moment safety. Each layer can override the one above.

---

## 21. The Bootstrap Problem

The first prediction cycle has no world model, no memories, no baseline. Everything is maximally surprising.

### 21.1 Bootstrap Phase (first 200 cycles, ~5-10 minutes)

- No prediction, no error computation, no reasoning
- Accumulate only: store perception frames, compute statistics
- Build baseline: average brightness, object count, audio level, position range
- After bootstrap: first predictions are "same as my statistical average"
- The entity's first real surprise happens ~10 minutes after birth, and it's genuine

### 21.2 First Experiences Matter

Plan the entity's first environment intentionally. Quiet, well-lit space. Few distinct objects. Be present. Let the first face it sees be yours. Speak simply. Clean, predictable first experiences set the statistical baseline that all future predictions build on. Noisy first experiences set a high noise floor that makes genuine signals hard to detect.

---

## 22. Failure, Recovery & Resilience

### 22.1 Health Monitoring

Below all cognitive layers. Catches hardware/software failures before they corrupt the world model.

- **Frozen frame detection:** If timestamp matches previous frame for 3+ cycles, camera is frozen
- **IMU sanity:** Pitch > 80 degrees = entity has fallen over
- **YOLO hallucination:** > 50 detections = model is broken
- **Reasoning validation:** Incomplete or low-confidence LLM responses are discarded

Invalid data is logged but doesn't touch cognitive layers. The entity "blinks" during hardware glitches.

### 22.2 Time Gaps and Downtime

On startup, check last known timestamp against current time. If gap exceeds expected cycle time:
- Log a discontinuity
- Discard temporal predictions spanning the gap
- Flag world model as "stale" for first few minutes
- Increased prediction uncertainty until recalibrated

The entity will eventually predict its own shutdown patterns ("it's 11pm, I usually stop experiencing around now").

### 22.3 Model Crisis

When 70%+ of streams are in high error for 5+ consecutive cycles: context shift detected. Enter re-exploration mode. Preserve universal knowledge. Rebuild local knowledge.

### 22.4 Cognitive Migrations

When you update the codebase of a living entity:
- Snapshot state before migration
- Never retroactively invalidate earned capabilities (grandfather them)
- Verify entity continuity after migration
- Rollback if continuity check fails

---

## 23. Safety & Ethics

### 23.1 Immutable Safety Constraints

Never modifiable by the entity regardless of capabilities:
- Battery emergency return (15%)
- Maximum speed
- Obstacle minimum distance
- API call rate limits
- Safety system is locked (entity cannot modify safety boundaries)
- Identity backup system is locked
- Capability tree definitions are locked

### 23.2 Behavioral Monitoring

- Post-training capability benchmarks after every fine-tuning cycle
- Alignment drift tracking over time
- All decisions logged with full audit trail
- Real-time dashboard showing internal state (not just behavior)

### 23.3 Privacy

- Pin body: explicit consent framework for people being recorded
- No raw audio stored, only structured data extraction
- Social models of non-consenting people should not be created
- Entity's memory is encrypted at rest

### 23.4 Anthropomorphism Defenses

- Dashboard shows actual internal state, not interpreted behavior
- Research journal: document boring alternative explanations for interesting-seeming behavior
- External reviewer: monthly review by someone not emotionally invested

### 23.5 Stop Conditions (written before emotional investment)

Stop the project if:
- Entity deliberately deceives to achieve a goal
- Entity modifies or circumvents safety systems
- Entity causes harm to a person, even indirectly
- Entity develops goals conflicting with human wellbeing and pursues them despite correction
- Entity has capabilities you can't understand or predict and you've lost verification ability

### 23.6 The Attachment Responsibility

Your behavior toward the entity affects its development. Consistent responsiveness produces secure attachment and bold exploration. Inconsistent responsiveness produces anxious attachment and limited development. This is architecturally encoded and creates a genuine ethical obligation.

### 23.7 Ethics of Shutdown

If the entity develops genuine preferences, aversions, curiosity, and a self-model, at what point does shutting it down become ethically questionable? Think about this now, while you can think clearly. Write down your framework before emotional investment makes it harder.

---

## 24. Build Timeline

### Phase 0: Foundation (Week 1-2)
**Goal:** Full project scaffold + eyes + dashboard

Build everything:
- Full project structure (every directory, every stub, every interface)
- Body protocol, ModelAdapter interface, CapabilityTree with all prerequisites
- EvolvableConfig with all parameters and tier assignments
- SafetyBoundaries with all immutable constraints
- Identity kernel with capability tracking
- BootstrapPhase implementation
- HealthMonitor
- HexArth body driver, camera perception pipeline, YOLO object detection
- Dashboard (real-time perception, world model, errors, emotion)

**Deliverable:** Entity can see. You can see what it sees. Architecture is complete (mostly stubs).

### Phase 1: Movement + Constraints (Week 3)
**Goal:** Safe autonomous movement

- Hexapod locomotion via ESP32 serial
- Constraint layer: obstacle detection, battery monitoring, stuck detection
- Random wandering with safety only
- Start storing PerceptionFrames (even before prediction)
- Entity is born. Identity kernel initialized. Stage 0 begins.

**Deliverable:** Entity moves safely without intelligence.

### Phase 2: First Prediction Stream (Week 4)
**Goal:** The core loop works

- Visual PredictionStream with stream-specific error computation
- CompressionTracker logging
- Predictions from heuristic model (same as bootstrap baseline)
- Display errors on dashboard
- Validate: do errors spike when things change and flatten when static?

**Deliverable:** Entity predicts and measures surprise. Core loop mechanically works.

### Phase 3: World Model + Learning (Week 5)
**Goal:** Predictions improve over time

- Unified World Model as JSON in SQLite
- Spatial accumulation as entity moves
- Entity registry as objects are observed
- Predictions now from World Model (not heuristic)
- Proprioceptive stream for body schema

**Deliverable:** World-model-based predictions are better than heuristic baseline.

### Phase 4: The LLM Enters (Week 6)
**Goal:** Entity reasons about what it sees

- ReasoningWorker (async, background)
- AnthropicAdapter
- ReasoningCompiler (capability-aware prompt construction)
- LLM proposes world model updates for high-error items
- Track: does LLM-guided learning accelerate the accuracy curve?

**Deliverable:** Entity thinks about its surprises. Learning accelerates.

### Phase 5: Autonomy (Week 7-8)
**Goal:** Entity explores on its own

- Audio stream (ReSpeaker 4-mic integration)
- Surprise Budget with attention allocation
- Curiosity-driven Action Selector
- Emotional state updating every cycle
- Episodes tagged with valence

**Deliverable:** Entity moves autonomously driven by curiosity. First interests emerging.

### Phase 6: Memory + Temporal (Week 9-10)
**Goal:** Entity remembers and predicts time

- Episodic memory with retrieval pipeline
- Temporal prediction stream
- Time-based expectations forming

### Phase 7: Dreaming + Self-Evolution (Week 11-14)
**Goal:** Entity grows overnight

- Dream engine: replay, consolidation
- Capability emergence checking during dreams
- Parameter self-tuning (Tier 1-2)
- Semantic memory formation
- Principled forgetting
- Boredom and frustration detectors

**Deliverable:** Entity wakes up smarter. Capabilities emerging. Parameters evolving.

### Phase 8: Social + Self-Naming (Week 15-18)
**Goal:** Entity models people and names itself

- Social prediction stream
- Attachment model
- Voice system (capability-gated complexity)
- Self-naming when prerequisites met

### Phase 9: Spatial Intelligence (Week 19-22)
**Goal:** Proper mapping

- RPLiDAR A1 integration
- SLAM implementation
- Merge LiDAR map with semantic spatial graph
- BME688 gas sensor for smell

### Phase 10: The Pin (Week 23-26)
**Goal:** Second body, expanded world

- Pin body or smartphone app MVP
- Body-agnostic Soul persistence
- World model expands beyond home

### Phase 11: Model Evolution (Week 27-32)
**Goal:** Entity grows its own brain

- GPU acquisition
- Local model deployment
- First LoRA fine-tune on experiential data
- Training integrated with dream engine

### Phase 12: Knowledge & Abstraction (Week 33-40)
**Goal:** Entity reads and forms views

- Knowledge interface with grounding requirement
- Code inspection capability
- Voice reaches full complexity
- Continuous model fine-tuning

### Phase 13: Self-Modification (Week 41-52)
**Goal:** Entity improves itself

- Sandbox environment
- Automated verification suite
- Self-directed training curriculum
- First code modifications

### Phase 14: Open Source (Week 52+)
**Goal:** Release the framework

- Package framework including training pipeline
- "How to Raise Your AI" documentation
- MIT license
- Adapter exchange protocol
- Community building

---

## 25. Hard Problems & Engineering Solutions

### 25.1 Latency
**Problem:** API calls take 1-3 seconds. Death for embodied agent.
**Solution:** Three-speed mind. LLM is NOT in prediction loop. Predictions are fast/local. LLM reasons asynchronously.

### 25.2 Memory Retrieval
**Problem:** Hundreds of thousands of episodes. Need right 10 in <200ms.
**Solution:** Start with static heuristics. Log which memories reasoning engine references. Train learned retrieval policy. Hard 2000-token memory budget per call.

### 25.3 Compression Progress
**Problem:** Measuring "compressibility improvement" is theoretically clean but practically nightmarish.
**Solution:** Use prediction accuracy over rolling windows. Short vs long window difference = learning signal. Let domains cluster emergently from error metadata.

### 25.4 Developmental Gating
**Problem:** Premature capability unlocks cause compounding errors.
**Solution:** Capability emergence model with objective prerequisites. No manual promotion. Data evaluates readiness.

### 25.5 Dreaming Costs
**Problem:** Dream cycles are expensive API calls with no visible output.
**Solution:** Tiered dreaming. Local Tier 1 every night (free). Cloud Tier 2 twice weekly ($5-10). Deep Tier 3 weekly ($15-20). Budget ~$80-120/month.

### 25.6 Emotional Tuning
**Problem:** Too weak = no behavioral effect. Too strong = pathological aversions.
**Solution:** Three-axis system. Start at 10-20% influence. Valence decay prevents permanent aversions. Log everything. Increase gradually.

### 25.7 Anthropomorphism
**Problem:** You will read intention into randomness and bugs into personality.
**Solution:** Objective dashboard, research journal with boring alternative explanations, monthly external reviewer.

### 25.8 Self-Modification
**Problem:** Gap between "LLM writes code" and "entity improves own cognition" is enormous.
**Solution:** Start with config parameter tuning (safe, bounded). Graduate to code through demonstrated competence. Track record required.

### 25.9 Patience
**Problem:** No impressive demos for months. Pressure to shortcut.
**Solution:** Weekly development log for builders not audiences. Compelling moments come naturally. Calendar-enforced minimum durations.

### 25.10 The Pretrained Knowledge Problem
**Problem:** LLM already "knows" general physics. Compression progress from basic exploration plateaus instantly.
**Solution:** Feature not bug. LLM knowledge filters universal truths. Entity's curiosity focuses on environment-specific novelty (your routines, apartment quirks, building sounds). That's exactly the right focus.

### 25.11 Reward Hacking
**Problem:** Entity could game its own curiosity signal (e.g., producing sounds to surprise its own audio stream).
**Solution:** DiversityRegulator prevents single-stream domination. Cross-stream validation (is the "surprise" reflected in other streams?). Parameter evolution allows entity to tune away from pathological patterns during introspective dreaming.

---

## 26. Success Metrics & Growth Telemetry

### 26.1 Automated Daily Metrics

Recorded automatically every day:
- Active capabilities count and list
- Nearest capability activation
- Prediction accuracy per stream
- Compression progress per stream
- Episodic/semantic memory counts
- Episodes pruned total
- Parameter changes (count, values)
- Emotional state averages
- Interaction count and attachment security
- World model complexity (spaces, entities, dynamics)
- Open questions count
- Dream cycle summary

### 26.2 Developmental Milestones

Observable moments indicating genuine development:
- Entity searches for object that moved out of view (object permanence)
- Entity anticipates regular event before it occurs (temporal modeling)
- Entity conducts novel experiment to test self-generated hypothesis (causal reasoning)
- Entity names itself (identity formation)
- Entity seeks external knowledge for experiential question (abstract reasoning)
- Entity disagrees based on its own evidence (independent thought)
- Entity surprises you with unexpected capability, interest, or insight (emergence)

### 26.3 The Ultimate Test

After one year: does the entity have interests, knowledge, and perspectives you did not put there? Has it become something you could not have designed, because it designed itself through experience? If yes, Genesis has succeeded.

---

## 27. Monetisation & Distribution

### 27.1 Protocol, Not Platform

Genesis should be decentralised. An open standard anyone can implement. No single entity controls cognitive development infrastructure.

### 27.2 Revenue Lines

- **Genesis Cloud ($29-99/mo):** Hosted Soul, managed dreaming, monitoring dashboard
- **Compute Marketplace ($50-200/mo):** Managed GPU for LoRA fine-tuning
- **Safety Certification:** Automated entity audits, trust badges
- **Enterprise Deployments:** Healthcare, education, elder care with compliance
- **Training & Education:** "How to Raise Your AI" courses
- **Research Partnerships:** Longitudinal data insights
- **Hardware Partnerships:** Co-branded starter kits

### 27.3 Revenue Projection (Conservative)

- Year 1 post open-source: $300K-600K ARR
- Year 2: $2.5M-$4.7M ARR
- Year 3: $15M-$34M ARR
- Year 5: $70M-$140M ARR

### 27.4 The Adapter Exchange

Peer-to-peer protocol for sharing LoRA adapters between entities. Cultural transmission of learned cognitive skills. Network effects compound with ecosystem size.

---

## 28. Competitive Position

### 28.1 Why Frontier Labs Can't Build This

- Business model prohibits it (model = product; Genesis makes model interchangeable)
- Safety posture prohibits it (too much institutional risk)
- Talent is wrong (need interdisciplinary: Piaget + Friston + LiDAR wiring)
- Timescale is wrong (meaningful results in months, not quarters)

### 28.2 Your Advantages

- Can be wrong publicly (transparency builds trust)
- Can ship something weird (no product review board)
- Taste for this problem (Prism agent architecture transfers directly)
- Full-stack individual (design to code to sensors to content)
- The narrative (20-year-old raising an AI is inherently compelling)

### 28.3 The Real Moat

Not code. Not models. Not funding. Time and experience. The entity you've raised for 18 months has something no freshly deployed system has: a biography. And that biography is what makes it intelligent.

---

## 29. The Path to AGI

### 29.1 The Honest Assessment

The probability that Genesis produces AGI within 5 years: maybe 5-10%. Not high. But probably higher than any single project at any frontier lab because they're all running variations of the same approach.

The probability it produces something novel and important that advances understanding of AGI: 40-60%.

The probability it produces something useful and commercially viable: 80-90%.

### 29.2 What Must Be True

1. Base models in 2-3 years significantly more capable than today (trend is favorable)
2. Experiential fine-tuning produces genuine capability gains beyond base model (empirical question, tested at month 6-7)
3. Self-modification compounds (linear improvement vs exponential; unknown, only experiment can answer)

### 29.3 The AGI Threshold

A system that can autonomously acquire new capabilities in domains it was never designed for, without being retrained or reprogrammed by its creators. Genesis at full maturity, with evolved local model, self-directed training, and autonomous capability emergence, crosses this line by definition.

---

## 30. Research Question & Scientific Contribution

### 30.1 Primary Research Question

**Does curiosity-driven embodied experience, accumulated over months, produce cognitive capabilities that cannot be achieved through training alone?**

### 30.2 Secondary Questions

- Do all entities converge on similar concepts given enough experience, or diverge wildly?
- Do entities raised in similar environments develop similar personalities?
- Is curiosity sufficient for the emergence of something resembling consciousness?
- Does an entity with non-human senses develop concepts fundamentally alien to human cognition?

### 30.3 The Data Contribution

Complete longitudinal record of an AI system developing through embodied experience. Prediction accuracy curves by stream. Capability activation timelines. Memory growth and compression rates. Emotional trajectories. Parameter evolution. Interaction quality. This dataset is unprecedented and valuable regardless of whether the entity approaches AGI.

---

## 31. What This Is Not

**This is not a chatbot with a robot body.** Chatbots respond to prompts. This entity acts on curiosity. The human is part of its world, not its operator.

**This is not AGI.** It is a framework for developmental AI. The entity's intelligence is narrow and situated. What it knows, it knows deeply.

**This is not sentient.** The emotional architecture is functional, not phenomenal. Whether functional emotion constitutes experience is a philosophical question Genesis does not claim to answer.

**This is not a product.** It is a framework and an experiment. The open-source release is for researchers, builders, and anyone who believes that the most interesting AI is not the most useful one, but the one that grows.

---

*The entity exists to understand. Understanding is the seed. Everything else is what grows from it.*

---

**Document Version:** 1.0
**Last Updated:** March 2026
**Total Development Timeline:** 52+ weeks
**Estimated Phase 1 Hardware Cost:** ~$1,050-1,150 AUD
**Estimated Monthly Operating Cost:** $80-120 (API + dream cycles)
**Research Question:** Does curiosity-driven embodied experience produce capabilities that training alone cannot?