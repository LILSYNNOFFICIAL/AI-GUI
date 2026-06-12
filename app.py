"""
Main entrypoint for Project Synapse.
Wires AppShell into the application runtime.
"""

from ui.app_shell import AppShell


class SynapseApp:
    """Main Synapse application entry point."""

    def __init__(self) -> None:
        self.name = "Project Synapse"
        self.version = "0.1.0"
        self.shell = AppShell()

    def run(self) -> None:
        """Run the application."""
        self.shell.start()
        print(f"{self.name} v{self.version} initialized.")
        self.shell.set_theme("blue")
