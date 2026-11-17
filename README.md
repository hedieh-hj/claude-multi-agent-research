# Claude Agents: Multi-Agent Research System

This repository contains the complete code and implementation for the **"Claude Agents: Build a Multi-Agent Research System in 7 Days"** course. 

* **Course Instructor:** Kesha Williams (via LinkedIn Learning)
* **Author / Implementer:** Hedieh Jamili

---

## 🚀 About the Project
This project builds an autonomous, multi-agent research system powered by Claude and the Claude Agent SDK. Instead of relying on a single conversational prompt, the architecture splits complex queries across specialized agents that search the web, analyze findings, resolve conflicting evidence, synthesize reports, evaluate quality, and run self-correction loops.

---

## 📅 7-Day Architecture Breakdown

- **Day 1: Search Agent**[cite: 1]  
  - Implements the foundational web search agent with budget controls (`max_budget_usd`), turn limits, and fallback models[cite: 1].
- **Day 2: Analysis Agent & Data Handoff**[cite: 3, 5]  
  - Introduces strict JSON schemas (`SEARCH_SCHEMA`) to guarantee safe, structured data handoff between the search agent and the analysis agent[cite: 3, 5].
- **Day 3: Dynamic Coordinator & Routing**  
  - Implements a coordinator agent (`AgentDefinition`) that breaks down multi-part user requests and dynamically routes tasks to specialized subagents.
- **Day 4: Conflict Resolution & Synthesis**  
  - Adds the `SYNTHESIS_AGENT` to merge multiple analyses, evaluate source corroboration and recency, and manage unresolved gaps.
- **Day 5: Polished Citation Reporting**  
  - Introduces the `REPORT_AGENT` to convert structured synthesis into a formal, cited Markdown research report with strict data lineage (`report.md`).
- **Day 6: Contract-Enforced Validation & Schemas**  
  - Enforces system-level contracts (`REPORT_SCHEMA`) with mechanical Python validation (`validate_report`) and reference pruning (`prune_unused_references`).
- **Day 7: Evaluator-in-the-Loop & Refinement Loop**  
  - Integrates an independent `EVALUATOR_AGENT` to grade reports on coverage, recency, and source diversity, triggering automatic follow-up research passes when gaps are identified.

---

## 🛠️ Requirements & Setup

1. Python 3.10 or later.
2. Install dependencies:
   ```bash
   pip install claude-agent-sdk
