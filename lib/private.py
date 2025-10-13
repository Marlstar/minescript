from lib.javatypes import Clazz

def get_field(clazz, field_name, super_class: bool=False): # type: ignore
    if super_class:
        c = clazz.getClass().getSuperclass()
    else:
        c = clazz.getClass()
    f = mappings.getRuntimeFieldName(c, field_name)
    field = c.getDeclaredField(f)
    field.setAccessible(True)
    return field.get(clazz)

def call_method(clazz, intermediary: str):
    methods = clazz.getClass().getDeclaredMethods()
    for method in methods:
        if method.getName() == intermediary:
            method.setAccessible(True)
            parameter_type = Array.newInstance(Clazz, 0)
            return method.invoke(clazz, parameter_type)
