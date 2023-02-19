import json
import os


def create_new_json(user_inf, key):
    with open('active.json', 'w') as f:
        json.dump({key: user_inf}, f, indent=4)


def write_to_json(user_id, floor, mash, mode, time, finish_time, progress):
    data = {'user_id': user_id, 'floor': floor, 'mash': mash, 'mode': mode,
            'time': time, 'finish_time': finish_time, 'progress': progress}
    key = f'{floor}.{mash}'
    if check_file(data, key):
        with open('active.json', 'r') as f:
            pepe = json.load(f)
        pepe[key] = data
        with open('active.json', 'w') as f:
            json.dump(pepe, f, indent=4)


def check_file(user_inf, key):
    if 'active.json' not in os.listdir():
        create_new_json(user_inf, key)
    else:
        return 1
