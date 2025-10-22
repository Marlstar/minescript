from lib.keybinds import Keybind
from lib.keyboard import KeyCode
from lib.exec import suspend, stop

Keybind.register(KeyCode.DELETE, stop)

def log_screen_id():
    from lib.screen import current
    print(current())

Keybind.register(KeyCode.INSERT, log_screen_id)

suspend()
