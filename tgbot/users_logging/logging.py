# каждый день создается новый файл с логами
import datetime
import json
import os
import asyncio


def create_new_json():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'w') as f:
        json.dump({}, f)


def write_to_json(user_id, floor, car_number, mode, time, finish_time, progress):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'r') as f:
        data = json.load(f)
    data[user_id] = {'floor': floor, 'car_number': car_number, 'mode': mode,
                     'time': time, 'finish_time': finish_time, 'progress': progress}
    with open(f'{today}_log.json', 'a') as f:
        json.dump(data, f, indent=4, default=str)


async def check_file():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if f'{today}_log.json' not in os.listdir():
        create_new_json()
    else:
        pass
