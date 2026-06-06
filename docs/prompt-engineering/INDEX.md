# AI Prompt Engineering Resource Index

This directory serves as the central hub for all AI prompt engineering documentation and templates within the RuVector repository.

## 📂 Directory Structure

- `docs/prompt-engineering/`: Core research, guides, and centralized documents.
- `docs/mega-prompts/`: Large system prompts and comprehensive prompt templates.
- `docs/prompt-engineering/google-drive/`: Destination for documents synced from Google Drive.

## 📝 Key Documents

### Prompt Engineering Research
- [DSPy Research Summary](DSPY_RESEARCH_SUMMARY.md): Overview of DSPy.ts research for Claude-Flow.
- [DSPy Comprehensive Research](DSPY_COMPREHENSIVE_RESEARCH.md): In-depth 50+ page technical analysis.
- [DSPy Quick Start Guide](DSPY_QUICK_START.md): 5-minute installation and setup guide.
- [Claude-Flow DSPy Integration](CLAUDE_FLOW_DSPY_INTEGRATION.md): Specific integration architecture.

### Implementation Guides
- [Agentic Synth DSPY Guide](AGENTIC_SYNTH_DSPY_GUIDE.md): Practical guide for DSPy integration in agentic workflows.

### Architecture Decision Records (ADRs)
- [ADR-009: Structured Output](ADR-009-structured-output.md): Decisions on grammar-constrained JSON generation.
- [ADR-010: Function Calling](ADR-010-function-calling.md): Standardizing tool use and function calling patterns.
- [ADR-011: Prefix Caching](ADR-011-prefix-caching.md): Optimizing prompt performance with prefix caching.

## 🚀 Mega Prompts

Located in `docs/mega-prompts/`:
- [rvAgent Base Prompt](../mega-prompts/RVAGENT_BASE_PROMPT.md): The core system prompt for the coding assistant.
- [Subagent Orchestration](../mega-prompts/SUBAGENT_ORCHESTRATION_PROMPTS.md): Prompts for task spawning and handoffs.
- [Skill Builder](../mega-prompts/SKILL_BUILDER_SYSTEM_PROMPT.md): Instructions for building Claude Code Skills.

## 🔄 Synchronization

To sync prompt engineering documents from your hard drive or Google Drive:
1. Ensure `rclone` or `gdrive` is installed.
2. Configure your credentials in `scripts/sync_gdrive_prompts.sh`.
3. Run the script: `./scripts/sync_gdrive_prompts.sh`.

---
*Last Updated: 2026-03-28*
