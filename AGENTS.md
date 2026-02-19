# Repository Guidelines

## Project Structure & Module Organization

`src/swing_mind/` contains the library code. `analyzer.py` is the entry point (`TennisAnalyzer`), with feature modules under `pose/`, `ball/`, `court/`, `shot/`, `action/`, `metrics/`, and shared helpers in `utils/`.

`tests/` contains unit tests (`test_*.py`) and `tests/conftest.py` for local import setup. `examples/` includes runnable demos such as `examples/basic_usage.py`. `docs/` holds reference docs (currently `docs/api.md`). Root files include `pyproject.toml`, `requirements.txt`, `README.md`, and `ROADMAP.md`.

## Build, Test, and Development Commands

- `uv sync --dev`: create/update the virtual environment and install project + dev dependencies.
- `uv run pytest -q`: run test suite.
- `uv run ruff format src tests examples`: format Python code.
- `uv run ruff check src tests`: run lint checks.
- `uv run python examples/basic_usage.py`: quick sanity check of public API usage.

## Coding Style & Naming Conventions

Use Python 3.10+ with 4-space indentation and PEP 8 defaults.

- Modules/files: `snake_case` (for example, `detector.py`).
- Classes: `PascalCase` (for example, `PoseDetector`).
- Functions/variables: `snake_case`.
- Tests: `test_<feature>.py` with test functions named `test_<behavior>()`.

Run `ruff format` before opening a PR; use `ruff check` to catch style and import issues.

## Testing Guidelines

Use `pytest` for unit tests. Place tests in `tests/` close to the target behavior and keep assertions focused on observable outputs. For new modules, add at least:

- initialization test
- happy-path behavior test
- edge/error-path test

No formal coverage threshold is configured yet; contributors should still expand coverage for modified code.

## Commit & Pull Request Guidelines

Follow concise, imperative commit messages, optionally with a prefix seen in history (for example, `Fix: ...`, `Remove ...`).

PRs should include:

- what changed and why
- related issue/roadmap item
- test evidence (`pytest` output)
- sample output snippets when analysis behavior changes (JSON fields, frame metadata, etc.)
