print("1")
from system.lib.java import eval_pyjinn_script
print("2")
from system.lib.minescript import screen_name
print("3")
from system.lib.minescript_runtime import render_loop
print("4")
import lib.mouse as mouse
print("5")
from lib.instance import mc
print("6")
from lib import net
print("7")

def current() -> str | None:
    name = screen_name()
    if name is None: return None
    return name.replace("net.minecraft.client.gui.screens.inventory.", "")

def wait_for_screen(target: str | list[str] | None = None):
    if isinstance(target, list) and len(target) == 0:
        target = None # Treat this like a wildcard

    while True:
        name = current()
        if name is not None:
            if isinstance(target, str) and name == target: break
            elif isinstance(target, list) and name in target: break
            else: break

_CLOSE_SCRIPT = eval_pyjinn_script(
"""
mc = JavaClass("net.minecraft.client.Minecraft").getInstance()
def close():
    screen = mc.screen
    if screen is not None:
        id = screen.getMenu().containerId
        mc.setScreen(None)
""")
_CLOSE_FN = _CLOSE_SCRIPT.get("close")
def close():
    screen = mc.screen
    if screen is not None:
        with render_loop:
            _CLOSE_FN()
            net.packet.send("ServerboundContainerClosePacket", id)
            mouse.set_grabbed(True)
