from typing import Any, Callable, final
from threading import Thread
from system.lib import minescript as ms
from lib.keyboard import Modifiers
from system.lib.minescript import EventQueue, KeyEvent

_NO_MODS = Modifiers.none()

Callback = Callable[[], Any]

@final
class Keybind:
    def __init__(self, key: int, mods: Modifiers, callback: Callback):
        self.key = key
        self.mods = mods
        self.callback = callback

        q = EventQueue()
        q.register_key_listener()
        self._thread = Thread(target=self._eventloop, args=[q], name=f"Keybind-{key}", daemon=True)
        self._thread.start()

    @staticmethod
    def register(key: int, callback: Callback, mods: Modifiers = _NO_MODS):
        bind = Keybind(key, mods, callback)
        _binds.append(bind)

    def _eventloop(self, queue: EventQueue):
        queue.register_key_listener()
        while True:
            event = queue.get(True)
            if event.action == 0 and event.key == self.key:
                self.callback()

_binds: list[Keybind] = []

def reset():
    _binds.clear()
