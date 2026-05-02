# llm-bench

LLM model x Coding agent benchmark. Compare generated web applications across different model and agent combinations using the same prompt.

## Concept

1. Define a prompt (task) with evaluation rubric
2. Generate apps using various **model x agent** combinations
3. Auto-evaluate with a fixed evaluator model (Claude Opus)
4. Compare scores in a matrix view

## Directory Structure

```
llm-bench/
├── prompts/                           # Task definitions
│   └── {id}-{slug}/
│       ├── prompt.md                  # Generation prompt
│       └── eval.md                    # Evaluation rubric
├── results/                           # Generated artifacts
│   └── {prompt_id}/
│       └── {model}_{agent}/
│           ├── meta.json              # Metadata (timestamp, versions)
│           └── app/                   # Generated application
├── evaluations/                       # Evaluation results
│   └── {prompt_id}/
│       └── {model}_{agent}.json       # Score and comments
├── templates/                         # Templates for new prompts
└── scripts/
    └── summary.py                     # Aggregate results
```

## Naming Conventions

| Item       | Format                  | Example                      |
|------------|-------------------------|------------------------------|
| Prompt ID  | `{NNN}-{slug}`          | `001-todo-app`               |
| Model      | lowercase kebab-case    | `claude-opus-4`, `gpt-4o`    |
| Agent      | lowercase kebab-case    | `claude-code`, `cursor`      |
| Result dir | `{model}_{agent}`       | `claude-opus-4_claude-code`  |

## Workflow

### 1. Create a prompt

Copy templates and fill in:

```bash
cp templates/prompt-template.md prompts/002-my-app/prompt.md
cp templates/eval-template.md prompts/002-my-app/eval.md
```

### 2. Generate an app

Use each model x agent combination to generate the app from the prompt. Save the result:

```
results/001-todo-app/claude-opus-4_claude-code/
├── meta.json   # fill from templates/meta-template.json
└── app/        # generated files go here
```

### 3. Evaluate

Use Claude Opus (fixed evaluator) to score the generated app. Each prompt has a ready-to-use evaluation prompt:

```bash
cat prompts/001-todo-app/eval-prompt.md
```

Paste the generated code into the `{paste ...}` section and send to the evaluator. Save the output JSON to:

```
evaluations/001-todo-app/claude-opus-4_claude-code.json
```

### 4. View results

```bash
python scripts/summary.py            # matrix table
python scripts/summary.py --detail   # with per-category breakdown
```

## Available Prompts

| ID              | Description        |
|-----------------|--------------------|
| `001-todo-app`  | Todo application   |
