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

def animated_loader(text, steps=10):
    for step in track(range(steps), description=text, style="bold_purple"):
        sleep(0.15)

def display_pulse_info():
    system_info = get_system_info()

    table = Table(title="[bold magenta]StylishFetch - Pulse Edition[/bold magenta]", style="bold cyan", box="SIMPLE")
    table.add_column("Component", style="bold magenta")
    table.add_column("Details", style="bold green")

    for key, value in system_info.items():
        table.add_row(f"[bold magenta]{key}[/bold magenta]", f"[bold green]{value}[/bold green]")

    console.print(table)

def main():
    console.print(Panel("[bold magenta]StylishFetch Pulse Edition - Beat of the system[/bold magenta]", expand=False))

    animated_loader("Pulsing system info...")

    display_pulse_info()

    console.print(Panel("[bold purple]System info loaded with a pulse![/bold purple]", expand=False))

if __name__ == "__main__":
    main()
