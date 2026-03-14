import threading
import subprocess
import asyncio
from status_alive import status_alive
import time
# SAMPLE set_interval(5.0, 'echo "This echo is delayed by 5.0 s and runs only once."', False) #

async def set_interval(interval, args, repeat):
    print('LINE  9')
    time.sleep(int(interval))
    subprocess.Popen(args)
    print('LINE 12')

    if repeat:
        print('LINE 15')
        await set_interval(interval, args, repeat)
