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
        "CPU Cores": psutil.cpu_count(logical=True),
        "RAM": f"{psutil.virtual_memory().total // (1024 ** 3)} GB",
    }
    return system_info

def animated_loader(text, steps=15):
    for step in track(range(steps), description=text, style="bright_cyan"):
        sleep(0.1)

def display_wave_info():
    system_info = get_system_info()

    table = Table(title="[bold cyan]StylishFetch - Wave Edition[/bold cyan]", style="bold cyan", box="DOUBLE_EDGE")
    table.add_column("Component", style="bold magenta")
    table.add_column("Details", style="bold white")

    for key, value in system_info.items():
        table.add_row(f"[bold magenta]{key}[/bold magenta]", f"[bold white]{value}[/bold white]")

    console.print(table)

def main():
    console.print(Panel("[bold cyan]Riding the system info wave...[/bold cyan]", expand=False))

    animated_loader("Fetching system details in waves...")

    display_wave_info()

    console.print(Panel("[bold blue]Wave of information complete![/bold blue]", expand=False))

if __name__ == "__main__":
    main()
