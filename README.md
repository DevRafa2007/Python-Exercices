# Python Learning Exercises

This repository contains a collection of Python exercises that I will complete as part of my curriculum and ongoing learning. The goal is to gather practical examples, small projects, and exercises that reinforce concepts learned during coursework and self-study.

## Repository structure

- Each exercise is a separate Python file in the repository root or a dedicated folder.
- Tests and helpers (if any) are included alongside exercises or in a `tests/` folder.
- Keep filenames descriptive so it's easy to find specific exercises.

## How to run an exercise

1. Open a terminal in the project folder.
2. Run an interactive exercise, for example:

   ```
   powershell> python .\ex1_media_tres_numeros.py
   ```

## Running tests (if provided)

- If there is a simple test runner, run:

  ```
  powershell> python .\test_runner.py
  ```

- Prefer minimal dependencies; use built-in `unittest` or `pytest` if available.

## Conventions and notes

- Exercises may use Portuguese variable names to match learning context, but code should be readable and consistent.
- Keep functions small and focused to make them easy to test and refactor.
- Simulated data should only be used for local testing, not for production or development environments that mimic production.

## Recommended next steps

- Add a `CONTRIBUTING.md` describing how to add new exercises and naming conventions.
- Add small README sections per folder for larger topic collections (e.g., `data-structures/`, `algorithms/`, `networking/`).
- Consider lightweight persistence or example inputs in a `fixtures/` folder for reproducible tests.

## License

- Add a license file if you plan to share the repository publicly.
