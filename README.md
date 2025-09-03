# CLRS Exercises (Introduction to Algorithms) — Python
3th Edition by:
Thomas H. Cormen
Charles E. Leiserson
Ronald L. Rivest
Clifford Stein

A skeleton repository with solutions to exercises and problems from the book "Introduction to Algorithms" (CLRS).**.
The structure is organized by chapters (`src/ChapterXX`), and files are named according to the exercise/problem
index in the style of `Exercise_2_2_2.py`, `Problem_2_1.py`, etc.

> **Task index source: MIT Press — Selected Solutions (pp. 82–83).  
> PDF: https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/selected-solutions.pdf

## Structure
```
src/
  Chapter01/
    Exercise_1_2_2.py
    Problem_1_1.py
    __init__.py
    ...
  Chapter02/
    Exercise_2_1_1.py
    Problem_2_1.py
    __init__.py
    ...
  Chapter03/
    Exercise_3_1_1.py
    Problem_3_1.py
    __init__.py
    ...
  Chapter04/
  ...
tests/
  Chapter01/
    test_exercise_1_2_1.py
    ...
  Chapter02/
    test_exercise_2_1_1.py
    test_problem_2_1.py
    ...
  Chapter03/
  ...
```

## Naming conventions
- Exercise files: `Exercise_X_Y_Z.py`
- Problem files: `Problem_X_Y.py`
- Each chapter is a folder `ChapterXX` (with leading zero).
- Each file should start with a short docstring describing the task.

## Quick start
```bash
# (optional) create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pytest -q
```

## Adding a new exercise
1. Find the task in the index (MIT Press Selected Solutions, pp. 82–83).
2. Create a file in the corresponding chapter folder, e.g. `src/Chapter02/Exercise_2_3_4.py.`.
3. Implement the solution and add tests in `tests/.`.
4. Run `pytest` to validate.

## Copyright and Source Guidelines
- This repository contains original implementations of the tasks by the author. Direct copying of other people's solutions is strictly prohibited.
- The README provides a link to the official Selected Solutions file, which serves solely as a reference for the task index.

***
## Uwaga o prawach autorskich i źródłach
- To repo zawiera **Twoje implementacje** zadań; nie kopiuj dosłownie cudzych rozwiązań.
- W README zawarto link do oficjalnego pliku *Selected Solutions* jako punktu odniesienia do indeksu zadań.
