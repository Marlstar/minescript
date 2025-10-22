print("m1")
from lib.instance import mc
print("m2")
from lib.javatypes import Minescript
print("m3")
_mappings = Minescript.mappingsLoader.get()
print("m4")

def set_grabbed(state: bool):
    clazz = mc.mouseHandler
    c = clazz.getClass()
    f = _mappings.getRuntimeFieldName(c, "mouseGrabbed")
    field = c.getDeclaredField(f)
    field.setAccessible(True)
    field.setBoolean(clazz, state)
