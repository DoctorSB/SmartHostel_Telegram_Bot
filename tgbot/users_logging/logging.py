# каждый день создается новый файл с логами
import datetime
import json
import os
import asyncio


def create_new_json():
    # создаем новый файл с логами
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'w') as f:
        json.dump({}, f)


def write_to_json(user_id, floor, car_number, mode, time):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'r') as f:
        data = json.load(f)
    data[user_id] = {'floor': floor,
                     'car_number': car_number, 'mode': mode, 'time': time}
    with open(f'{today}_log.json', 'w') as f:
        json.dump(data, f)


async def check_file():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if f'{today}_log.json' not in os.listdir():
        create_new_json()
    else:
        pass
