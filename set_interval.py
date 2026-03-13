import threading
import os
from status_alive import status_alive

# SAMPLE set_interval(5.0, 'echo "This echo is delayed by 5.0 s and runs only once."', False) #

def run_command(interval, command, repeat):
    os.system(command)
    if repeat:
        t = threading.Timer(interval, run_command, args=[interval, command, repeat])
        t.start()

def set_interval(interval, command, repeat):
    t = threading.Timer(interval, run_command, args=[interval, command, repeat])
    t.start()
    status_alive()
