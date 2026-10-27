# Turkey Adapter — Starter

Canonical teaching example for the **Adapter** pattern.

The existing client is written against the `Duck` contract. `WildTurkey` has useful behavior, but exposes a different interface and different flight semantics.

Use this repository to follow the class discussion before the Adapter is introduced. The completed reference implementation is in `adapter-turkey-solution`.

## Course conventions

- Python is only the implementation language; the pattern roles are language-agnostic.
- One main class per source file.
- Object Adapter / composition is the primary form used in this course.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
