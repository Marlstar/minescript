from lib.instance import mc

def set_grabbed(state: bool):
    clazz = mc.mouseHandler
    c = clazz.getClass()
    f = mappings.getRuntimeFieldName(c, "mouseGrabbed")
    field = c.getDeclaredField(f)
    field.setAccessible(True)
    field.setBoolean(clazz, state)
