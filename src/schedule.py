import os
import sys
import json
from submodules.set_interval import set_interval
import asyncio
from submodules.status_alive import status_alive
from submodules.sample_json import SAMPLE_JSON
from submodules.get_time_diff import get_time_diff

SCHEDULE_FILE = 'schedule.json'

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

    task1 = asyncio.create_task(set_interval(0, [], False))
    task2 = asyncio.create_task(set_interval(0, [], False))
    task3 = asyncio.create_task(set_interval(0, [], False))

    for item in schedule_data:
        if 'timeout' in item:
            task1 = asyncio.create_task(set_interval(int(item['timeout']), item['sh'], False))
        if 'interval' in item:
            task2 = asyncio.create_task(set_interval(int(item['interval']), item['sh'], True))
        if 'moment' in item:
            given_moment = item['moment']
            calculated_timeout = get_time_diff(given_moment)
            if calculated_timeout == None:
                print('Sorry, configuration contains an invalid moment: ' + given_moment)
                sys.exit()
            task3 = asyncio.create_task(set_interval(calculated_timeout, item['sh'], False))

    await task1
    await task2
    await task3
    status_alive()

asyncio.run(main())
