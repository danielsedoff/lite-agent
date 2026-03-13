import os
import json
from set_interval import set_interval

SCHEDULE_FILE = 'schedule.json'

def load_schedule_file():
    if os.path.exists(SCHEDULE_FILE):
        try:
            with open(SCHEDULE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    else:
        with open(SCHEDULE_FILE, 'w', encoding='utf-8') as f:
            json.dump([{
                  "interval": 2,
                  "sh": "ls"
                },{
                  "timer": 3,
                  "sh": "echo 12345"
                },{
                  "timer": 10,
                  "sh": "echo HELLO"
                }], f, indent=4)

schedule_data = load_schedule_file()
if schedule_data != None and len(schedule_data) > 0:
    for item in schedule_data:
        if 'timer' in item:
            set_interval(int(item['timer']), item['sh'], False)
        if 'interval' in item:
            set_interval(int(item['interval']), item['sh'], True)
