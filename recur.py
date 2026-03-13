import os
import json
from set_interval import set_interval

RECUR_FILE = 'recur.json'

def load_recur_file():
    if os.path.exists(RECUR_FILE):
        try:
            with open(RECUR_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    else:
        with open(RECUR_FILE, 'w', encoding='utf-8') as f:
            json.dump([{
                  "interval": 2,
                  "sh": "ls"
                },{
                  "timer": 3,
                  "sh": "echo 12345"
                }], f, indent=4)

recur_data = load_recur_file()
if recur_data != None and len(recur_data) > 0:
    for item in recur_data:
        if 'timer' in item:
            set_interval(int(item['timer']), item['sh'], False)
        if 'interval' in item:
            set_interval(int(item['interval']), item['sh'], True)
