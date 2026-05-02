# llm-bench - Claude Code Rules

## Project Overview

Benchmark repository comparing LLM models x coding agents. Same prompt -> different combinations -> auto-evaluate.

## Naming Conventions

- Prompt IDs: `{NNN}-{slug}` (e.g., `001-todo-app`)
- Model names: lowercase kebab-case (e.g., `claude-opus-4`, `gpt-4o`, `gemini-2.5-pro`)
- Agent names: lowercase kebab-case (e.g., `claude-code`, `cursor`, `copilot`, `cline`)
- Result directories: `{model}_{agent}` (underscore separator)

## Directory Layout

- `prompts/{id}/prompt.md` — generation prompt
- `prompts/{id}/eval.md` — evaluation rubric
- `results/{prompt_id}/{model}_{agent}/app/` — generated app files
- `results/{prompt_id}/{model}_{agent}/meta.json` — generation metadata
- `evaluations/{prompt_id}/{model}_{agent}.json` — evaluation scores

## Evaluation

- Evaluator model: Claude Opus (fixed, for consistency)
- Scoring: 100 points total (functionality 30, code quality 25, UI/UX 25, creativity 20)
- Output format: JSON matching the schema in `templates/eval-template.md`

## When Generating Apps for Benchmarks

- Follow the prompt constraints exactly (e.g., single HTML file, no CDN)
- Fill in `meta.json` with accurate timestamps and version info
- Place all generated files under `app/` subdirectory

## When Evaluating

- Read both `prompt.md` and `eval.md` before scoring
- Score each category independently
- Be consistent across evaluations — use the rubric, not subjective impressions
