from system.lib.minescript import echo_json

ROSEWATER = "#f5e0dc"
FLAMINGO = "#f2cdcd"
PINK = "#f5c2e7"
MAUVE = "#cba6f7"
RED = "#f38ba8"
MAROON = "#eba0ac"
PEACH = "#fab387"
YELLOW = "#f9e2af"
GREEN = "#a6e3a1"
TEAL = "#94e2d5"
SKY = "#89dceb"
SAPPHIRE = "#74c7ec"
BLUE = "#89b4fa"
LAVENDER = "#b4befe"
TEXT = "#cdd6f4"
SUBTEXT1 = "#bac2de"
SUBTEXT0 = "#a6adc8"
OVERLAY2 = "#9399b2"
OVERLAY1 = "#7f849c"
OVERLAY0 = "#6c7086"
SURFACE2 = "#585b70"
SURFACE1 = "#45475a"
SURFACE0 = "#313244"
BASE = "#1e1e2e"
MANTLE = "#181825"
CRUST = "#11111b"

def echo_coloured(text: str, colour: str):
    _ = echo_json([{"text":text, "color":colour}])

def _scope(scope: str | None) -> str:
    if scope is not None:
        return f"[{scope}] "
    else: return ""

def error(text: str, scope: str | None = None):
    echo_coloured(f"{_scope(scope)}{text}", RED)

def warn(text: str, scope: str | None = None):
    echo_coloured(f"{_scope(scope)}{text}", YELLOW)

def notify(text: str, scope: str | None = None):
    echo_coloured(f"{_scope(scope)}{text}", BLUE)
