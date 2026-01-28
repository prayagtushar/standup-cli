import datetime
import os
import shutil
import tempfile
from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError


def is_github_url(path: str) -> bool:
    return (
        path.startswith("https://github.com/") or 
        path.startswith("git@github.com:") or
        path.startswith("https://") and ".git" in path or
        path.startswith("git://")
    )


def clone_repo(repo_url: str) -> str:
    try:
        temp_dir = tempfile.mkdtemp(prefix="standup_")
        
=        Repo.clone_from(repo_url, temp_dir)
        
        return temp_dir
    except GitCommandError as e:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise ValueError(f"Failed to clone repository: {str(e)}")
    except Exception as e:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise ValueError(f"Error cloning repository: {str(e)}")


def cleanup_temp_repo(repo_path: str) -> None:
    """
    Clean up temporary cloned repository.
    
    Args:
        repo_path: Path to temporary repository
    """
    try:
        if os.path.exists(repo_path) and repo_path.startswith(tempfile.gettempdir()):
            shutil.rmtree(repo_path)
    except Exception:
        pass


def is_valid_repository(repo_path: str) -> bool:
    """
    Check if the provided path is a valid git repository (local or URL).
    
    Args:
        repo_path: Local path or GitHub URL to check
        
    Returns:
        True if valid git repository, False otherwise
    """
    if is_github_url(repo_path):
        return True
    
    try:
        if os.path.exists(repo_path):
            Repo(repo_path)
            return True
    except InvalidGitRepositoryError:
        pass
    
    return False


def get_recent_commits(repo_path: str = ".", days: int = 1, author_name: str = None) -> list[dict]:
    """
    Fetches commit messages from the last N days for a specific author.
    Supports both local repositories and GitHub URLs.
    
    Args:
        repo_path: Path to local git repository or GitHub URL
        days: Number of days to look back
        author_name: Optional author name filter (case-insensitive substring match)
        
    Returns:
        List of commit dictionaries with hexsha, message, date, and author
    """
    temp_repo_path = None
    
    try:
        if is_github_url(repo_path):
            temp_repo_path = clone_repo(repo_path)
            actual_repo_path = temp_repo_path
        else:
            actual_repo_path = repo_path
        
        repo = Repo(actual_repo_path)
        
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)

        commits = []
        for commit in repo.iter_commits():
            commit_date = commit.committed_datetime.replace(tzinfo=None)
            if commit_date < cutoff_date:
                continue

            if author_name and author_name.lower() not in commit.author.name.lower():
                continue

            commits.append({
                "hexsha": commit.hexsha[:7],
                "full_hash": commit.hexsha,
                "message": commit.message.strip(),
                "author": commit.author.name,
                "email": commit.author.email,
                "date": commit.committed_datetime.strftime("%Y-%m-%d %H:%M")
            })
        
        return commits

    except InvalidGitRepositoryError:
        raise ValueError(f"Error: '{repo_path}' is not a valid git repository")
    except ValueError as e:
        raise e
    except Exception as e:
        raise RuntimeError(f"Error reading git repo: {e}")
    finally:
        if temp_repo_path:
            cleanup_temp_repo(temp_repo_path)