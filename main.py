"""
Standup-CLI: Daily Standup Auto-Generator

This CLI tool scans a git repository and generates formatted standup summaries
from commit history.
"""

import sys
import typer
from rich.console import Console
from rich.table import Table
import pyperclip

from git_utils import get_recent_commits, is_valid_repository
from parser import group_commits_by_category, format_standup

app = typer.Typer(
    help="Generate daily standup summaries from git commits",
    invoke_without_command=True,
    no_args_is_help=False,
)
console = Console()


def run_generate(
    days: int = None,
    author: str = None,
    path: str = None,
    copy: bool = False,
):
    if path is None:
        path = typer.prompt("Enter repository path or public GitHub URL", default=".")
    
    if days is None:
        days = typer.prompt("Enter number of days to look back", default=1, type=int)

    if author is None:
        author = typer.prompt("Filter by author (leave empty for all)", default="", show_default=False)
        if not author:
            author = None
    
    if not is_valid_repository(path):
        console.print(f"[red]Error: '{path}' is not a valid git repository[/red]")
        raise typer.Exit(code=1)
    
    console.print(
        f"[bold cyan]Scanning repo at {path} for the last {days} day(s)...[/bold cyan]"
    )
    
    try:
        commits = get_recent_commits(repo_path=path, days=days, author_name=author)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(code=1)
    
    if not commits:
        console.print("[yellow]No commits found for this period.[/yellow]")
        return
    
    console.print(f"[green]Found {len(commits)} commit(s)[/green]\n")
    
    table = Table(title="Recent Activity", show_header=True, header_style="bold magenta")
    table.add_column("Hash", style="cyan", no_wrap=True)
    table.add_column("Time", style="yellow")
    table.add_column("Author", style="green")
    table.add_column("Message", style="white", width=50)

    for commit in commits:
        table.add_row(
            commit["hexsha"],
            commit["date"],
            commit["author"],
            commit["message"][:50] + "..." if len(commit["message"]) > 50 else commit["message"]
        )

    console.print(table)
    
    grouped = group_commits_by_category(commits)
    standup_text = format_standup(grouped)
    
    console.print("\n[bold]--- Standup Summary ---[/bold]")
    console.print(standup_text)
    
    console.print("\n[bold]--- Statistics ---[/bold]")
    console.print(f"Total Commits: {len(commits)}")
    for cat, items in grouped.items():
        if items:
            console.print(f"{cat}: {len(items)}")

    if copy:
        try:
            pyperclip.copy(standup_text)
            console.print("\n[bold green]✓ Copied to clipboard![/bold green]")
        except Exception as e:
            console.print(f"[yellow]Warning: Could not copy to clipboard: {e}[/yellow]")


@app.command()
def generate(
    days: int = typer.Option(None, "--days", "-d", help="Number of days to look back"),
    author: str = typer.Option(None, "--author", "-a", help="Filter by author name"),
    path: str = typer.Option(None, "--path", "-p", help="Path to the git repository"),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy result to clipboard"),
):
    """Generate a standup summary from recent git commits."""
    run_generate(days, author, path, copy)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    days: int = typer.Option(None, "--days", "-d", help="Number of days to look back"),
    author: str = typer.Option(None, "--author", "-a", help="Filter by author name"),
    path: str = typer.Option(None, "--path", "-p", help="Path to the git repository"),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy result to clipboard"),
):
    """
    Standup-CLI: Daily Standup Auto-Generator
    """
    if ctx.invoked_subcommand is None:
        run_generate(days, author, path, copy)


@app.command()
def config():
    """Show current configuration."""
    console.print("[bold]Standup-CLI Configuration[/bold]")
    console.print("  Default days: 1")
    console.print("  Default path: . (current directory)")
    console.print("  Author filter: Optional")


if __name__ == "__main__":
    app()


@app.command()
def config():
    """Show current configuration."""
    console.print("[bold]Standup-CLI Configuration[/bold]")
    console.print("  Default days: 1")
    console.print("  Default path: . (current directory)")
    console.print("  Author filter: Optional")


if __name__ == "__main__":
    app()