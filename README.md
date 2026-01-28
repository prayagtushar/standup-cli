# Standup-CLI: The Daily Standup Auto-Generator

## Project Overview

**Standup-CLI** is a Python-based command-line tool designed to automate the daily routine of writing "Standup Updates" for software developers.

It scans a Git repository (local or remote GitHub URL), retrieves the commit history, and formats it into a clean, categorized list suitable for standup meetings.

## Features

- **GitHub Support:** Provide a GitHub URL to scan public repositories.
- **Auto-Grouping:** Automatically categorizes commits based on prefixes (feat, fix, docs, etc.).
- **Interactive Mode:** Prompts for a repository path or URL if not provided.
- **Clipboard Integration:** Optionally copy the generated summary to your clipboard.
- **Beautiful Output:** Uses `rich` for formatted tables and colors.

## Tech Stack

- **Language:** Python 3.10+
- **CLI Framework:** `typer`
- **UI/Output:** `rich`
- **Git Interaction:** `GitPython`
- **Clipboard:** `pyperclip`

## Installation

1. Clone this repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

Run the CLI using:
```bash
python main.py [OPTIONS]
```

### Options:

- `--days` / `-d`: (Integer, Default: 1) Number of days to look back.
- `--author` / `-a`: (String, Optional) Filter commits by a specific author name.
- `--path` / `-p`: (String, Optional) Path to the local git repository or GitHub URL.
- `--copy` / `-c`: (Boolean flag) Automatically copy the result to the clipboard.

### Examples:

```bash
# Scan current directory
python main.py

# Scan a specific local path
python main.py --path /path/to/repo

# Scan a GitHub repository
python main.py --path https://github.com/psf/requests --days 7

# Filter by author and copy to clipboard
python main.py -a "John Doe" -c
```

## Project Structure

```text
standup-cli/
├── main.py           # Entry point and CLI command definitions.
├── git_utils.py      # Git operations (local and remote).
├── parser.py         # Commit message categorization logic.
├── requirements.txt  # Project dependencies.
└── README.md         # Project documentation.
```# standup-cli
