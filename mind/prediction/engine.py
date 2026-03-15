"""Prediction engine — the core cycle. FAST, LOCAL, DETERMINISTIC.

No API calls. No async. No network. Predictions come from the World Model.
The LLM is called asynchronously by ReasoningWorker when errors exceed threshold.

Build phase: 0.4 (Week 4)
"""
