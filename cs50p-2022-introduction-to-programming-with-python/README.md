# CS50P 2022 — Introduction to Programming with Python

Solutions, notes, and projects completed while working through **CS50's Introduction to Programming
with Python (CS50P)**, Harvard/edX's course on Python fundamentals.

## About the Course

CS50P is an introductory course that teaches programming using Python — covering functions,
variables, conditionals, loops, exceptions, libraries, unit testing, file I/O, regular expressions,
and object-oriented programming.

- **Course:** CS50's Introduction to Programming with Python
- **Provider:** Harvard University (via edX / CS50.harvard.edu)
- **Language:** Python 3.14.6

## Repository Structure

```text
cs50p-2022-introduction-to-programming-with-python/
├── src/                        # chapter/lecture-wise code
│   ├── week00_functions_variables/
│   │   ├── indoor_voice.py
│   │   └── agree.py
│   ├── week01_conditionals/
│   ├── week02_loops/
│   ├── week03_exceptions/
│   ├── week04_libraries/
│   ├── week05_unit_tests/
│   │   └── test_something.py
│   ├── week06_file_io/
│   ├── week07_regex/
│   ├── week08_oop/
│   └── week09_et_cetera/
├── resources/                  # datasets, sample inputs, images used in exercises
│   ├── data.csv
│   └── sample_input.txt
├── final_project/              # standalone final project submission
│   ├── project.py
│   ├── test_project.py
│   └── README.md
├── requirements.txt
├── .gitignore
└── README.md
```

> Adjust the structure above to match your actual folder layout (by week, by problem set, etc.).

## How to Run

Each folder contains standalone Python scripts. To run any file:

```bash
python3 filename.py
```

Some problem sets include test files (e.g. `test_filename.py`) that can be run with `pytest`:

```bash
pip install pytest
pytest test_filename.py
```

## Setting Up a Virtual Environment

It's recommended to use a virtual environment to keep this project's dependencies isolated from your
system Python.

```bash
# Create and enter project directory
mkdir my-project
cd my-project

# Create virtual environment
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install packages as you need them
pip install requests
pip install python-dotenv
pip install locust

# Or install packages from requirements.txt file
pip install -r requirements.txt

# After installing packages, freeze them
pip freeze > requirements.txt

# Deactivate virtual environment
deactivate
```

## Development Setup — Black + Optimize Imports (IntelliJ/PyCharm)

### 1. Install Black

Install Black in your project's virtual environment (make sure `venv` is activated):

```bash
pip install black
```

If you're tracking dependencies, add it to your `requirements.txt` (or keep it in a separate
`requirements-dev.txt` since Black is a dev-only tool):

```bash
pip freeze > requirements.txt
```

### 2. Enable "Run Black" on Save

1. Go to **Settings/Preferences → Tools → Actions on Save**
2. Check the box next to **Run Black**
3. Close the project and restart the IDE to ensure Black is detected in your virtual environment.
4. IntelliJ will auto-detect the Black package installed in your interpreter (shown as _"Using Black
   package vX.X.X"_)
5. Click **Apply** Now every time you save a `.py` file, Black will auto-format it — including
   converting single quotes to double quotes, fixing line length, spacing, and trailing commas.

### 3. Enable "Optimize Imports" on Save

1. In the same **Actions on Save** screen, check the box next to **Optimize imports**
2. Click **Apply** This automatically:

- Removes unused imports
- Sorts imports alphabetically
- Cleans up import formatting
  > Note: "Optimize imports" removes _unused_ imports and sorts existing ones — it does **not** add
  > new imports automatically as you type.
  >
  > For auto-adding imports while typing, use **Alt+Enter** (Windows/Linux) or **Option+Enter**
  > (Mac) as a quick-fix when you reference an undefined name. You can also enable **Settings →
  > Editor → General → Auto Import** for single-import suggestions.

### 4. Save and Verify

Open any `.py` file, add an unused import or a messy string with single quotes, hit **Cmd+S /
Ctrl+S**, and confirm:

- Unused imports disappear
- Quotes convert to double quotes
- Code reformats per Black's style

## Requirements

- Python 3.10+
- (List any third-party libraries used, e.g. `pytest`, `requests`, etc.)

Install dependencies (if applicable):

```bash
pip install -r requirements.txt
```

## Progress

| Problem Set                   | Status |
| ----------------------------- | ------ |
| Week 0 – Functions, Variables | ✅     |
| Week 1 – Conditionals         | ✅     |
| Week 2 – Loops                | ⬜     |
| Week 3 – Exceptions           | ⬜     |
| Week 4 – Libraries            | ⬜     |
| Week 5 – Unit Tests           | ⬜     |
| Week 6 – File I/O             | ⬜     |
| Week 7 – Regular Expressions  | ⬜     |
| Week 8 – OOP                  | ⬜     |
| Final Project                 | ⬜     |

## Academic Honesty

This repository is for **personal learning and portfolio purposes**. If you're currently taking
CS50P, please don't copy this code directly — refer to
[CS50's Academic Honesty policy](https://cs50.harvard.edu/p/2022/honesty/) and do your own work.

## License

This project is licensed under the MIT License — feel free to reference or learn from it.

## Author

Deepjyoti Barman / Senior QAE - II @ MakeMyTrip /
[@deepjyoti-barman](https://github.com/deepjyoti-barman) / Bangalore, Karnataka, India.
