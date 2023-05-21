import json
import os
import datetime


def create_new_json(user_inf, key):
    with open('active.json', 'w') as f:
        json.dump({key: user_inf}, f, indent=4)


def write_to_json(log):
    data = {'user_id': log.id, 'floor': log.floor, 'mash': log.mash, 'start_time': log.time, 'finish_time': log.finish_time, 'progress': log.progress, 'sushu': log.sushu}
    key = f'{log.floor}.{log.mash}'
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


def delete_json():
    with open(f'active.json', 'r') as f:
        pepe = json.load(f)
    del_list = []
    for key in pepe:
        if pepe[key]['finish_time'] == datetime.datetime.now().strftime("%d-%m-%Y %H:%M"):
            del_list.append(key)
        elif pepe[key]['finish_time'] < datetime.datetime.now().strftime("%d-%m-%Y %H:%M"):
            del_list.append(key)
    for elem in del_list:
        pepe.pop(elem)
    with open(f'active.json', 'w') as f:
        json.dump(pepe, f, indent=4)
