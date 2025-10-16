from lib.instance import mc
from lib.javatypes import Minescript
_mappings = Minescript.mappingsLoader.get()

def set_grabbed(state: bool):
    clazz = mc.mouseHandler
    c = clazz.getClass()
    f = _mappings.getRuntimeFieldName(c, "mouseGrabbed")
    field = c.getDeclaredField(f)
    field.setAccessible(True)
    field.setBoolean(clazz, state)
