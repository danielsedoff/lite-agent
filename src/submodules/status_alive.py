import sys
import time

def status_alive():
    while True:
        for i in range(4):
            sys.stdout.write(f"\rScheduler is up and running{'.' * i}   ")
            sys.stdout.flush()
            time.sleep(0.5)
