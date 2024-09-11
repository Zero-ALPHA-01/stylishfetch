import os
import platform
import psutil
from time import sleep
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel

console = Console()

def get_system_info():
    uname = platform.uname()
    system_info = {
        "Operating System": f"{uname.system} {uname.release}",
        "Processor": uname.processor,
        "Architecture": platform.architecture()[0],
        "Python Version": platform.python_version(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "RAM": f"{psutil.virtual_memory().total // (1024 ** 3)} GB",
    }
    return system_info

def animated_loader(text, steps=12):
    for step in track(range(steps), description=text, style="bright_magenta"):
        sleep(0.1)

def display_glow_info():
    system_info = get_system_info()

    table = Table(title="[bold yellow]Glow StylishFetch[/bold yellow]", style="bold magenta", box="HEAVY")
    table.add_column("Component", style="bold cyan")
    table.add_column("Details", style="bold green")

    for key, value in system_info.items():
        table.add_row(f"[bold cyan]{key}[/bold cyan]", f"[bold green]{value}[/bold green]")

    console.print(table)

def main():
    console.print(Panel("[bold cyan]Welcome to StylishFetch Glow Edition[/bold cyan]", expand=False))

    animated_loader("Fetching glowing system details...")

    display_glow_info()

    console.print(Panel("[bold red]All info loaded with glow![/bold red]", expand=False))

if __name__ == "__main__":
    main()
