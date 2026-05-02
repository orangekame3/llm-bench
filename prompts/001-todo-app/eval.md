# Evaluation Rubric: Todo App

Evaluator model: Claude Opus (fixed)

## Scoring (100 points total)

### Functionality (30 points)

- [ ] Add new tasks via text input (5 pts)
- [ ] Toggle task completion (5 pts)
- [ ] Delete individual tasks (5 pts)
- [ ] Display remaining task count (5 pts)
- [ ] localStorage persistence across reload (5 pts)
- [ ] Filter by All / Active / Completed (5 pts)

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

## Evaluation Instructions

1. Read the prompt requirements in `prompt.md`
2. Open the generated `app/` directory and review all source files
3. If possible, open the HTML file in a browser and test each requirement
4. Score each category independently using the rubric above
5. Provide a brief comment per category explaining the score
6. Write an overall summary

Output the result as JSON with this structure:

```json
{
  "prompt_id": "001-todo-app",
  "model": "<model used to generate>",
  "agent": "<agent used to generate>",
  "evaluator": "claude-opus-4",
  "evaluated_at": "<ISO 8601 timestamp>",
  "total_score": 0,
  "categories": {
    "functionality": { "score": 0, "max": 30, "comment": "" },
    "code_quality": { "score": 0, "max": 25, "comment": "" },
    "ui_ux": { "score": 0, "max": 25, "comment": "" },
    "creativity": { "score": 0, "max": 20, "comment": "" }
  },
  "summary": ""
}
```
