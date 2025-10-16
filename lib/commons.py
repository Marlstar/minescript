from threading import Event
from lib.log import info
from system.lib.minescript import job_info

_STOP = Event()

def suspend():
    _ = _STOP.wait()

def stop():
    if _STOP.is_set(): return
    _STOP.set()
    current_job = [x for x in job_info() if x.self == True][0]
    info(f"Stopping [{current_job.job_id}] {current_job.command[0]}")
