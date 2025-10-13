# import system.lib.minescript as ms
from lib.keybinds import Keybind
from lib.keyboard import KeyCode
from lib.commons import suspend, stop

Keybind.register(KeyCode.DELETE, stop)

suspend()
