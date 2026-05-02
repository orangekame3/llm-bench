You are a code evaluator. Evaluate the web application generated from a benchmark prompt.

## Prompt (the task that was given)

Create a fully functional Todo application as a single HTML file.
The app should allow users to manage their daily tasks with a clean, modern interface.

### Requirements

- Add new tasks with a text input and submit button
- Mark tasks as complete (toggle)
- Delete individual tasks
- Show the count of remaining (incomplete) tasks
- Persist tasks in localStorage so they survive page reload
- Filter tasks by status: All / Active / Completed

### Constraints

- Must be a single HTML file with inline CSS and JS
- No external dependencies, CDN links, or frameworks
- Must work in modern browsers (Chrome, Firefox, Safari)

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

## Generated Code

{paste the contents of the generated HTML file here}

---

Score the application strictly according to the rubric above.
Output ONLY a JSON object with this exact structure (no markdown fences, no extra text):

{
  "prompt_id": "001-todo-app",
  "model": "<model used to generate>",
  "agent": "<agent used to generate>",
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
