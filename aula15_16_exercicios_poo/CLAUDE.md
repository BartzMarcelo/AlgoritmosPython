# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Educational Python repository for an algorithms/programming course. Content is organized by lesson (`aula`) folders covering fundamentals through OOP, plus a `python_essential_1` section with supplementary material.

## Language

All code comments, variable names, class names, and user-facing strings are in **Brazilian Portuguese**. Follow this convention when writing or modifying code.

## Running Code

Scripts are standalone Python files. Run any exercise directly:

```bash
python <path_to_file>.py
```

No build system, package manager, or virtual environment is used. No dependencies beyond the Python standard library.

## Project Structure

- `aula01` through `aula17_*` — Lesson folders, numbered sequentially by topic (snake_case, zero-padded):
  - aula01–06: Fundamentals (types, functions, conditionals, operators, vectors, loops)
  - aula07–12: Loops (`for`, `while`)
  - aula13–16: OOP (classes, attributes, methods, `__init__`, `__str__`)
  - aula17: Lists and tuples
- `python_essential_1/` — Supplementary exercises and notes (includes `modulo4/` with markdown study notes on functions, tuples, dicts, exceptions)
- `revisao_ferias/`, `exercicios_fixacao_classes/` — Review/practice exercises
- `notas/` — General notes (Git commands, VS Code shortcuts, misc annotations)

## Code Conventions

- OOP exercises use a **two-file pattern**: a class definition module (e.g., `classeContaBancaria.py`) and a `main.py` that imports and uses it with `if __name__ == '__main__'`.
- Type hints are used on `__init__` parameters and return types (e.g., `def __init__(self, modelo: str, cor: str, ano: int) -> None`).
- Classes use `__str__` for display and f-strings for formatted output.
