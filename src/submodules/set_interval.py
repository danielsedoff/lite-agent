import subprocess
import asyncio
# SAMPLE set_interval(5.0, 'echo "This echo is delayed by 5.0 s and runs only once."', False) #

async def set_interval(interval, args, repeat):
    if len(args) == 0: return
    await asyncio.sleep(interval)
    subprocess.Popen(args)
    if repeat:
        await set_interval(interval, args, repeat)
