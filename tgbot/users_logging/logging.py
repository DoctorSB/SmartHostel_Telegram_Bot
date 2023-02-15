# каждый день создается новый файл с логами
import datetime
import json
import os
# import asyncio


def create_new_json(megapivo, key):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'w') as f:
        json.dump({key: megapivo}, f, indent=4)


def write_to_json(user_id, floor, car_number, mode, time, finish_time, progress):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # with open(f'{today}_log.json', 'r') as f:
    #     data = json.load(f)
    data = {'floor': floor, 'car_number': car_number, 'mode': mode,
            'time': time, 'finish_time': finish_time, 'progress': progress}
    key = floor + '.' + car_number
    if check_file(data, key):
        with open(f'{today}_log.json', 'r') as f:
            pepe = json.load(f)
        pepe[key] = data
        with open(f'{today}_log.json', 'w') as f:
            json.dump(pepe, f, indent=4)


def check_file(megapivo, key):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if f'{today}_log.json' not in os.listdir():
        create_new_json(megapivo, key)
    else:
        return 1


def main():
    print('pivo')
    user_id = '123'
    floor = '1'
    mode = 'mode'
    time = 'time'
    finish_time = 'finish_time'
    progress = 'progress'
    # create_new_json()
    write_to_json(user_id, floor, '1', mode,
                  time, finish_time, progress)
    write_to_json(user_id, floor, '2', mode,
                  time, finish_time, progress)


if __name__ == '__main__':
    main()
