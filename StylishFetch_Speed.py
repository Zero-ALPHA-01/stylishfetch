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

def animated_loader(text, steps=5):
    for step in track(range(steps), description=text, style="bright_yellow"):
        sleep(0.05)

def display_speed_info():
    system_info = get_system_info()

    table = Table(title="[bold yellow]StylishFetch - Speed Edition[/bold yellow]", style="bold green", box="HEAVY_EDGE")
    table.add_column("Component", style="bold blue")
    table.add_column("Details", style="bold red")

    for key, value in system_info.items():
        table.add_row(f"[bold blue]{key}[/bold blue]", f"[bold red]{value}[/bold red]")

    console.print(table)

def main():
    console.print(Panel("[bold yellow]StylishFetch Speed Edition - Fast and Efficient[/bold yellow]", expand=False))

    animated_loader("Quickly fetching system info...")

    display_speed_info()

    console.print(Panel("[bold red]All system info loaded at lightning speed![/bold red]", expand=False))

if __name__ == "__main__":
    main()
