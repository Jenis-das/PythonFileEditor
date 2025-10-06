# Mini Python File Manager

A simple **Command-Line File Manager** built in Python to perform basic file operations like Create, Read, Update, and Delete (CRUD). Perfect for learning Python file handling and basic CLI interactions.

---

## **Features**

* **View Files**

  * Read entire file, single line, or all lines.
  * Specify reading mode (`read`, `readL`, `readLs`).

* **Write Files**

  * Overwrite file content safely.
  * Warns before overwriting existing data.

* **Edit / Append Files**

  * Append new content without deleting existing data.
  * Supports simple editing using `r+` or `a+` mode.

* **File Creation & Management**

  * Create new files if they don’t exist.
  * Switch between multiple files easily.
  * View current file name.

* **Cursor Operations**

  * Know current cursor position (`tell`).
  * Move cursor to a specific location (`seek`).

* **Exit Command**

  * Clean exit from the program.

---

## **Commands**

| Command       | Description                   |
| ------------- | ----------------------------- |
| `view`        | View file content (read mode) |
| `w`           | Write / overwrite file        |
| `a` or `edit` | Append or edit file           |
| `x`           | Create a new file             |
| `new`         | Switch to a new file          |
| `fileName`    | Show current file name        |
| `tell`        | Show cursor position          |
| `seek`        | Move cursor position          |
| `readL`       | Read a single line            |
| `readLs`      | Read all lines                |
| `exit`        | Exit the program              |

---

## **Usage**

1. Run the script:

```bash
python file_manager.py
```

2. Type `view` to see available commands and start interacting.

3. Enter your file name when prompted.

4. Choose your operation and follow the on-screen instructions.

---

## **Requirements**

* Python 3.x
* No external libraries required (uses standard `os` module).

---

## **Notes**

* Write mode (`w`) **overwrites** file content. Be careful.
* Edit mode (`a`/`r+`) preserves existing data and appends new input.
* This project is meant for learning and experimentation with **file handling** and **CLI applications** in Python.

---

## **Author**

**Jenis Das (JD)** – Passionate about Python, microcontrollers, and creating innovative projects.

