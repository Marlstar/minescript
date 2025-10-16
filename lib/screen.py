from system.lib.minescript import screen_name
import lib.mouse as mouse
from lib.instance import mc
from system.lib.minescript_runtime import render_loop
from lib import net

def wait_for_screen(target: str | list[str] | None = None):
    if isinstance(target, list) and len(target) == 0:
        target = None # Treat this like a wildcard

    while True:
        name = screen_name()
        if name is not None:
            if isinstance(target, str) and name == target: break
            elif isinstance(target, list) and name in target: break
            else: break


def close():
    screen = mc.screen
    if screen is not None:
        with render_loop:
            id = screen.getMenu().containerId
            mc.setScreen(None)
            net.packet.send("ServerboundContainerClosePacket", id)
            mouse.set_grabbed(True)
