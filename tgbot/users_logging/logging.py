# каждый день создается новый файл с логами
import datetime
import json
import os
# import asyncio


def create_new_json(user_inf, key):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'w') as f:
        json.dump({key: user_inf}, f, indent=4)


def write_to_json(user_id, floor, mash, mode, time, finish_time, progress):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    data = {'user_id': user_id, 'floor': floor, 'mash': mash, 'mode': mode,
            'time': time, 'finish_time': finish_time, 'progress': progress}
    key = floor + '.' + mash
    if check_file(data, key):
        with open(f'{today}_log.json', 'r') as f:
            pepe = json.load(f)
        pepe[key] = data
        with open(f'{today}_log.json', 'w') as f:
            json.dump(pepe, f, indent=4)


def check_file(user_inf, key):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if f'{today}_log.json' not in os.listdir():
        create_new_json(user_inf, key)
    else:
        return 1
