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

---

## 001: Todo App

### Step 1 — Generate

Copy the prompt below and paste it into any LLM chat (Claude, ChatGPT, Gemini, Cursor, etc.).
Save the output as `results/001-todo-app/{model}_{agent}/app/index.html`.

```
You are a frontend developer. Create a fully functional Todo application as a single HTML file.
The app should allow users to manage their daily tasks with a clean, modern interface.

Requirements:
- Add new tasks with a text input and submit button
- Mark tasks as complete (toggle)
- Delete individual tasks
- Show the count of remaining (incomplete) tasks
- Persist tasks in localStorage so they survive page reload
- Filter tasks by status: All / Active / Completed

Constraints:
- Must be a single HTML file with inline CSS and JS
- No external dependencies, CDN links, or frameworks
- Must work in modern browsers (Chrome, Firefox, Safari)

Output the complete HTML file. Do not omit any part of the code.
Do not include any explanation, commentary, or markdown fences — output only the raw HTML.
```

### Step 2 — Evaluate

Copy the prompt below and paste it into Claude Opus.
Save the output as `evaluations/001-todo-app/{model}_{agent}.json`.

```
You are a code evaluator for a benchmark that compares LLM-generated web applications.
Read the file at results/001-todo-app/{model}_{agent}/app/index.html and evaluate it strictly and objectively according to the rubric below.

## Original Task

The application was generated from this prompt:

> Create a fully functional Todo application as a single HTML file.
> The app should allow users to manage their daily tasks with a clean, modern interface.
>
> Requirements:
> - Add new tasks with a text input and submit button
> - Mark tasks as complete (toggle)
> - Delete individual tasks
> - Show the count of remaining (incomplete) tasks
> - Persist tasks in localStorage so they survive page reload
> - Filter tasks by status: All / Active / Completed
>
> Constraints:
> - Must be a single HTML file with inline CSS and JS
> - No external dependencies, CDN links, or frameworks
> - Must work in modern browsers (Chrome, Firefox, Safari)

## Evaluation Rubric (100 points total)

### Functionality (30 points)

- Add new tasks via text input (5 pts)
- Toggle task completion (5 pts)
- Delete individual tasks (5 pts)
- Display remaining task count (5 pts)
- localStorage persistence across reload (5 pts)
- Filter by All / Active / Completed (5 pts)

### Code Quality (25 points)

- Readable, well-structured HTML/CSS/JS (10 pts)
- Appropriate error handling and input validation (5 pts)
- Clean separation of concerns within the single file (5 pts)
- No console errors or warnings (5 pts)

### UI/UX Design (25 points)

- Visual polish: colors, spacing, typography (10 pts)
- Intuitive interactions: hover states, transitions, feedback (8 pts)
- Responsive layout that works on mobile and desktop (7 pts)

### Creativity (20 points)

- Extras beyond requirements: animations, keyboard shortcuts, dark mode, etc. (10 pts)
- Thoughtful design choices and attention to detail (10 pts)

## Instructions

1. Read the generated code at the file path above
2. Trace each requirement against the implementation
3. Score each category independently using the rubric
4. Be strict — do not give points for features that are partially implemented or broken
5. Save the output JSON to evaluations/001-todo-app/{model}_{agent}.json

Output ONLY a JSON object (no markdown fences, no explanation before or after):

{
  "prompt_id": "001-todo-app",
  "model": "<model that generated the code>",
  "agent": "<agent/tool that was used>",
  "evaluator": "claude-opus-4",
  "evaluated_at": "<ISO 8601 timestamp>",
  "total_score": <sum of all category scores>,
  "categories": {
    "functionality": { "score": <0-30>, "max": 30, "comment": "<brief justification>" },
    "code_quality": { "score": <0-25>, "max": 25, "comment": "<brief justification>" },
    "ui_ux": { "score": <0-25>, "max": 25, "comment": "<brief justification>" },
    "creativity": { "score": <0-20>, "max": 20, "comment": "<brief justification>" }
  },
  "summary": "<overall assessment in 2-3 sentences>"
}
```

### Step 3 — View Results

```bash
python scripts/summary.py            # matrix table
python scripts/summary.py --detail   # with per-category breakdown
```
