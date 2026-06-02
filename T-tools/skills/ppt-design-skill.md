# PPT Design Skill

**Trigger:** Use this skill whenever creating PowerPoint presentations, pitch decks, investor slides, or client presentations.

**Full skill location:** `<workspace-root>/T-tools/ppt-design-skill/`

## Reference Files

| Goal | Path |
|------|------|
| Design system & philosophy | `T-tools/ppt-design-skill/references/systems.md` |
| Layout patterns | `T-tools/ppt-design-skill/references/layouts.md` |
| Color & typography | `T-tools/ppt-design-skill/references/visual-language.md` |
| pptxgenjs API | `T-tools/ppt-design-skill/references/pptxgenjs.md` |

## Mandatory Workflow

1. **Read `references/systems.md` first** — design philosophy and non-negotiables
2. **Answer 3 questions before touching code:**
   - What ONE emotional response should the audience feel?
   - What visual world matches that emotion? (editorial / cinematic / executive / bold / organic)
   - What layout motif repeats on every slide?
3. **Define a Design System object** before building any slide
4. **Visual QA** — render every slide to image, inspect, fix, re-render

## Core Non-Negotiables

- One motif on every slide (structural, not decorative)
- No accent lines under titles — use whitespace and color blocks
- Size contrast creates hierarchy (36–44pt title / 14–16pt body)
- Dominant color = 60–70% visual weight
- Every slide must earn its place — if it can be cut, cut it

## Dependency

```bash
npm install -g pptxgenjs
```
