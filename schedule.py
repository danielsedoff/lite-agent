import os
import sys
import json
from set_interval import set_interval
import asyncio

SCHEDULE_FILE = 'schedule.json'
SAMPLE_JSON = [{ "interval": 2, "sh": "ls" }, { "timeout": 3, "sh": "echo 1"},{ "timeout": 10, "sh": "echo 2" }]

def load_schedule_data():
    if os.path.exists(SCHEDULE_FILE):
        try:
            with open(SCHEDULE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    else:
        with open(SCHEDULE_FILE, 'w', encoding='utf-8') as f:
            json.dump(SAMPLE_JSON, f, indent=4)

async def main():
    schedule_data = load_schedule_data()
    if schedule_data == None or len(schedule_data) < 1:
        print('schedule.json is empty or invalid. Quitting')
        sys.exit()

    for item in schedule_data:
        if 'timeout' in item:
            print(1111122)
            asyncio.create_task(set_interval(int(item['timeout']), item['sh'], False))
        if 'interval' in item:
            print(1111133)
            asyncio.create_task(set_interval(int(item['interval']), item['sh'], True))

asyncio.run(main())
