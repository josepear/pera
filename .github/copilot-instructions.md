# Copilot instructions

## Repo purpose

This repository contains the Pera backend for Gabinet.

## Workflow rules

- Work on `dev`, not on `main`, unless explicitly asked.
- Keep API changes explicit and predictable.
- Avoid broad refactors unless they are required by the task.
- Do not change auth or token behavior casually.

## Editing rules

- Prefer simple, maintainable Python.
- Preserve existing structure unless there is a clear improvement.
- Keep validation, auth and error handling consistent.
- Do not introduce dependencies without a strong reason.

## Validation

Before finishing, check:

- routes still match expected behavior
- auth flow is not weakened
- imports are clean
- the change stays inside the intended scope
