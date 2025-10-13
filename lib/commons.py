from threading import Event

_STOP = Event()

def suspend():
    _ = _STOP.wait()

def stop():
    _STOP.set()
