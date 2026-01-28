"""
Parser module for commit message categorization.
"""

CATEGORY_KEYWORDS = {
    "✨ Features": ["feat", "add", "new", "feature"],
    "🐛 Bug Fixes": ["fix", "bug", "hotfix", "bugfix"],
    "🔧 Maintenance": ["docs", "chore", "refactor", "style", "cleanup", "test"],
}


def extract_prefix(message: str) -> str:
    """Extract the first word/prefix from a commit message."""
    if not message:
        return ""
    parts = message.split()
    if not parts:
        return ""
    # Remove colons if present (e.g., "feat:" -> "feat")
    return parts[0].lower().rstrip(":")


def categorize_commit(message: str) -> str:
    """
    Categorize a commit message based on its prefix.
    Returns the category name or "📝 Other Changes" if no match found.
    """
    prefix = extract_prefix(message)
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        if prefix in keywords:
            return category
    
    return "📝 Other Changes"


def clean_message(message: str) -> str:
    """Clean and format a commit message."""
    return message.strip().replace("\n", " ")


def group_commits_by_category(commits: list[dict]) -> dict[str, list[dict]]:
    """
    Group commits by their category.
    
    Args:
        commits: List of commit dictionaries
        
    Returns:
        Dictionary with categories as keys and list of commits as values
    """
    grouped = {
        "✨ Features": [],
        "🐛 Bug Fixes": [],
        "🔧 Maintenance": [],
        "📝 Other Changes": [],
    }
    
    for commit in commits:
        category = categorize_commit(commit["message"])
        grouped[category].append(commit)
    
    return grouped


def format_standup(grouped_commits: dict[str, list[dict]]) -> str:
    """
    Format grouped commits into a standup-friendly markdown string.
    
    Args:
        grouped_commits: Dictionary of commits grouped by category
        
    Returns:
        Formatted markdown string
    """
    output = []
    
    for category, commits in grouped_commits.items():
        if commits:  # Only include categories that have commits
            output.append(f"\n{category}")
            for commit in commits:
                output.append(f"  - {clean_message(commit['message'])}")
    
    return "".join(output)
