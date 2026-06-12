"""
Theme system for Project Synapse.
Provides simple blue/black theme definitions and application.
"""

from typing import Dict, Any


class ThemeEngine:
    """Basic theme engine supporting multiple UI themes."""

    def __init__(self) -> None:
        self._themes: Dict[str, Dict[str, Any]] = {
            "blue": {
                "background": "#001f3f",
                "foreground": "#ffffff",
                "accent": "#0074D9",
            },
            "black": {
                "background": "#000000",
                "foreground": "#00ffcc",
                "accent": "#111111",
            },
        }
        self._current_theme: str = "blue"

    def apply_theme(self, name: str) -> Dict[str, Any]:
        """Apply a theme by name."""
        if name not in self._themes:
            raise KeyError(f"Theme '{name}' not found")

        self._current_theme = name
        return self._themes[name]

    def get_theme(self) -> Dict[str, Any]:
        """Return the current theme."""
        return self._themes[self._current_theme]

    def list_themes(self) -> Dict[str, Dict[str, Any]]:
        """Return all available themes."""
        return self._themes
