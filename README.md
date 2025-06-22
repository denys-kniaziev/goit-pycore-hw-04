# Woolf University. Python Programing Course. Homework – File Operations and Modular System

## Overview

This assignment covers working with text files, directory traversal, and building a simple CLI assistant. You will implement functions to process salary records, parse cat data, visualize directory structures with color, and build a console-based helper bot.

---

## Task 1 – Total and Average Salary

### Description

You have a text file where each line contains a developer’s surname and monthly salary, separated by a comma (no spaces). Example:

```
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

Write a function `total_salary(path)` that reads this file and returns a tuple:

1. Total sum of all salaries.
2. Average salary.

### Requirements

* `total_salary(path: str) -> (int, float)`
* Read the file at `path` (specify encoding if needed).
* Compute total and average salary.
* Return `(total, average)`.

### Tips

* Use `with open(path, encoding='utf-8') as f:`
* Split each line on `','`.
* Handle missing file or read errors with try/except.

### Evaluation Criteria

* Correct total and average calculation.
* Proper error handling for missing or corrupted file.
* Clean, well-structured, documented code.

### Example

```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Total: {total}, Average: {average}")  # Total: 6000, Average: 2000
```

---

## Task 2 – Parse Cats Info

### Description

A text file contains cat records: `id,name,age` per line. Example:

```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
...
```

Write `get_cats_info(path)` to read the file and return a list of dictionaries:

```python
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    ...
]
```

### Requirements

* `get_cats_info(path: str) -> List[Dict[str, str]]`
* Read file, split lines on commas.
* Build dict with keys `id`, `name`, `age` for each line.
* Handle file read errors.

### Tips

* Use `with open(path, encoding='utf-8') as f:`
* For each line: `id_, name, age = line.strip().split(',')`
* Append `{"id": id_, "name": name, "age": age}` to result list.

### Evaluation Criteria

* Accurate parsing into list of dicts.
* Proper exception handling.
* Clean, maintainable code.

### Example

```python
cats = get_cats_info("cats.txt")
print(cats)
```

---

## Task 3 – Directory Structure Visualizer

### Description

Create a script that takes a directory path as a command-line argument and prints its tree structure (folders and files). Use colors to distinguish directories from files.

### Requirements

* Use a Python virtual environment.
* Script name example: `hw03.py`.
* Use `sys.argv` or `argparse` to get the path.
* Use `pathlib` to walk the directory (recursively or iteratively).
* Use `colorama` for colored output.
* Handle invalid path or non-directory errors.

### Tips

1. Create and activate a venv: `python -m venv .venv && source .venv/bin/activate`.
2. Install `colorama` via `pip install colorama`.
3. Use `Path(path).rglob('*')` or `os.walk()`.
4. Prefix directories with one color, files with another.

### Evaluation Criteria

* Virtual environment setup and usage.
* Correct path argument handling.
* Accurate tree display with recursion.
* Proper colored output with `colorama`.
* Code quality and readability.

### Example

```bash
$ python hw03.py /path/to/directory
```

Should print something like:

```
picture/
  Logo/
    IBM+Logo.png
    ibm.svg
  bot-icon.png
  mongodb.jpg
```

(Directories and files in different colors)

---

## Task 4 – Console Assistant Bot

### Description

Build a simple CLI assistant that parses commands and manages a contact book (name → phone). The bot supports adding, changing, showing contacts, listing all, and exiting.

### Supported Commands

* `hello` → prints “How can I help you?”
* `add <name> <phone>` → saves a new contact.
* `change <name> <new_phone>` → updates existing contact.
* `phone <name>` → shows the contact’s phone or an error if missing.
* `all` → lists all contacts.
* `close` or `exit` → prints “Good bye!” and terminates.
* Any other input → “Invalid command.”

### Requirements

* Implement `main()` for the REPL loop (input/print only there).
* Implement `parse_input()` to split command and args (case-insensitive).
* Handlers: `add_contact()`, `change_contact()`, `show_phone()`, `show_all()`.
* Store contacts in a Python dict.
* Clean separation: parsing, handlers, and I/O.

### Tips

* `cmd, *args = user_input.split()` → `cmd = cmd.lower()`.
* Each handler takes `args` and `contacts` and returns a response string.
* In `main()`, loop until `cmd` in `['exit','close']`.

### Evaluation Criteria

* REPL loop with prompt, case-insensitivity.
* Correct behavior for all commands.
* Handlers separate from I/O.
* Graceful handling of missing or malformed arguments.
* Clean, commented code.
