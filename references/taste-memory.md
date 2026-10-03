# Taste memory: what gets remembered, where, and who wins

Purpose: three memory layers, a strict precedence order, and the rules for logging and promoting keep/reject decisions.
Reach for `style-lock-format.md` instead when you need the lock's field schema.

## The three layers

| Layer | Path | Holds | Write when |
|---|---|---|---|
| Project lock | `.frontend-design/style-lock.md` | This project's tokens, structure, effects, imagery recipe, avoid list | A choice becomes a project rule |
| Decision log | `.frontend-design/decisions.log` | Append-only kept / rejected / pending-review evidence | After every design pass |
| Profile | `~/.frontend-design/profile.md` | Durable cross-project preferences | Only on a resolved, reusable decision |

## Precedence (strict, highest first)
1. The current user request.
2. `.frontend-design/style-lock.md`.
3. Resolved (`kept` or `rejected`) entries in `.frontend-design/decisions.log`.
4. `~/.frontend-design/profile.md`.

Pending-review entries guide review only. They never count as approval, never override a lower layer, and never get promoted.

## Read order
- Fresh project: read the profile before `01-system.md`. State the 1-3 priors you apply. Still ground the project in its own brief.
- Existing project: read the lock first. Use the profile only where the lock is silent.
- Follow-up session: read pending entries first. Resolve the one that touches the new work before building.
- Profile vs request conflict: follow the request, log the new decision.
- Profile vs lock conflict: follow the lock, mention the conflict if it matters.
- Do not let memory narrow range early. Use it to skip known rejects, then still explore.

## Decision log format
One JSON object per line. See `templates/decisions.log` for the header.

```json
{"ts":"<ISO-8601>","project":"<repo-root path>","screen":"<screen or component>","status":"kept|rejected|pending-review","axis":"palette|type|density|structure|effects|imagery|copy|interaction|other","decision":"<specific choice>","why":"<reason>","source":"user|agent-pending|migration","promote":false}
```

Examples:
```json
{"ts":"2026-09-16T10:00:00+05:30","project":"/repo","screen":"homepage hero","status":"kept","axis":"structure","decision":"one promise, one explanation, two actions, one product visual","why":"user preferred a clean first impression over a feature-dense hero","source":"user","promote":true}
{"ts":"2026-09-16T10:06:00+05:30","project":"/repo","screen":"dashboard empty state","status":"pending-review","axis":"imagery","decision":"line illustration tinted to locked accent","why":"keeps the shell calm, avoids an asset-empty state","source":"agent-pending","promote":false}
```

An existing plain-text log stays plain text. New projects use JSONL.

## Capture rules
- Ask one concrete keep/reject question per pass: "keep this hero density, or try a quieter variant?" Never "thoughts?"
- User answers: log `status` with `source: "user"`.
- Nobody to answer (autonomous run): log `status: "pending-review"`, `source: "agent-pending"`. Include reasoning. Do not claim approval.
- User later resolves a pending entry: append a new kept/rejected line that references it. Never edit old lines.
- Log at build-useful resolution: "36px table rows" is useful, "looks nice" is not.

## Promotion rules
Promote to `~/.frontend-design/profile.md` only when:
- The user explicitly says carry it forward, or
- The same preference appears in 2+ resolved entries across screens or projects, or
- It describes a reusable axis: density, motion feel, typography taste, imagery style, shape language, hierarchy, common rejects.

Never promote:
- Pending-review entries.
- One-off brand constraints or client/sponsor/platform-forced choices.
- Fallbacks caused by missing assets, missing tools, or time pressure.
- Anything the user accepted with hesitation.

## Profile format

```markdown
# frontend-design profile

Updated: <date>

## Strong priors
- Density: <preference> (evidence: <project>, <date>, <decision>)
- Motion: <preference> (evidence: ...)
- Type: <preference> (evidence: ...)

## Things to avoid
- <rejected pattern> (evidence: <project>, <date>)

## Open questions
- <preference needing one more resolved decision>
```

Remove or contradict an entry only when a newer resolved decision supports it.

## Handoff (every task)
State three facts: `decisions.log` changed or not, `style-lock.md` changed or not, `profile.md` changed or not and why. Memory is local files on the user's machine, nothing hosted.

Distilled from:
- /Users/rakeshbhugra/code/frontend-skills/tastemaker/skills/tastemaker/references/taste-memory.md
