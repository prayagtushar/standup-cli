# Standup-CLI: The Daily Standup Auto-Generator

**Standup-CLI** is a terminal tool that generates daily standup summaries from git commit history. It supports local repositories and public GitHub URLs, automatically categorizing your work into Features, Bug Fixes, and Maintenance.

## 🚀 Quick Start

### Installation

Choose one of the following methods:

**Option 1: From PyPI (Recommended)**
```bash
pip install standup-cli
standup-cli
```

**Option 2: From Homebrew (macOS)**
```bash
brew tap prayagtushar/standup-cli
brew install standup-cli
standup-cli
```

**Option 3: From GitHub**
```bash
pip install git+https://github.com/prayagtushar/standup-cli.git
standup-cli
```

**Option 4: Development Setup**
```bash
git clone https://github.com/prayagtushar/standup-cli.git
cd standup-cli
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 🛠 Usage & Options

You can also bypass the prompts by providing arguments directly:

```bash
python main.py [OPTIONS]
```

| Option | Shorthand | Description |
| :--- | :--- | :--- |
| `--path` | `-p` | Local folder path or public GitHub URL |
| `--days` | `-d` | Number of days to look back (default: 1) |
| `--author`| `-a` | Filter by author name (substring match) |
| `--copy`  | `-c` | Automatically copy the summary to clipboard |

### Examples:

- **Scan a GitHub Repo:**
  `python main.py -p https://github.com/psf/requests -d 7`
- **Scan Current Folder:**
  `python main.py` (then press Enter for defaults)
- **Filter by Name & Copy:**
  `python main.py -a "Alice" -c`

## 📊 Features

- **Interactive Mode:** Guides you through setup if no arguments are provided.
- **Auto-Categorization:** Uses commit message prefixes (feat, fix, docs, etc.) to group your updates.
- **GitHub Support:** Clones public repositories to a temporary folder to scan them.
- **Rich Formatting:** Beautiful tables and colored output for better readability.
- **Statistics:** Provides a quick count of your activity by category.

## 📂 Project Structure

- `main.py`: The entry point and CLI logic.
- `git_utils.py`: Logic for cloning and reading git history.
- `parser.py`: Logic for categorizing and formatting commit messages.
- `requirements.txt`: Project dependencies.