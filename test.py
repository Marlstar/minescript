from lib.keybinds import Keybind
from lib.keyboard import KeyCode
from lib.exec import suspend, stop
from lib.screen import wait_for_screen, close
from lib import log

def screen():
    print("running")
    log.info("Waiting for screen")
    wait_for_screen(["Crafting", "Creative Inventory"])
    log.info("Found screen")
    import time
    time.sleep(1)
    close()


log.info("registering keybinds")
Keybind.register(KeyCode.DELETE, stop)
log.info("halfway")
Keybind.register(KeyCode.INSERT, screen)
log.info("registered")

suspend()
