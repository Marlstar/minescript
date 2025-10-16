from system.lib.minescript import screen_name
import lib.log as log

def wait_for_screen(target: str | list[str] | None = None):
    if isinstance(target, list) and len(target) == 0:
        target = None # Treat this like a wildcard

    while True:
        name = screen_name()
        if name is not None:
            if isinstance(target, str) and name == target: break
            elif isinstance(target, list) and name in target: break
            else: break
