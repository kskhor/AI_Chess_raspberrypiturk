# unused - is only necessary if running on Raspberry Turk hardware. Otherwise, it must be removed or modified.
from raspberryturk import is_running_on_raspberryturk, RaspberryTurkError

if not is_running_on_raspberryturk():
    raise RaspberryTurkError("Must be running on Raspberry Turk to use {} module.".format(__name__))
