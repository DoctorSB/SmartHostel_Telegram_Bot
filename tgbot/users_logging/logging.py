# каждый день создается новый файл с логами
import datetime
import json
import os
# import asyncio


def create_new_json():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'w') as f:
        json.dump({}, f, indent=4)


def write_to_json(user_id, floor, car_number, mode, time, finish_time, progress):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # with open(f'{today}_log.json', 'r') as f:
    #     data = json.load(f)
    data = {'floor': floor, 'car_number': car_number, 'mode': mode,
            'time': time, 'finish_time': finish_time, 'progress': progress}
    # print(data)
    key = floor + '.' + car_number
    check_file(data, key)
    with open(f'{today}_log.json', 'r') as f:
        pepe = json.load(f)
    pepe[key] = data
    with open(f'{today}_log.json', 'w') as f:
        json.dump(pepe, f, indent=4)


def check_file(megapivo, key):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if f'{today}_log.json' not in os.listdir():
        create_new_json()
    else:
        return 1


def delete_json():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f'{today}_log.json', 'r') as f:
        pepe = json.load(f)
    del_list = []
    for key in pepe:
        if pepe[key]['finish_time'] == datetime.datetime.now().strftime("%d-%m-%Y %H:%M"):
            del_list.append(key)
    for elem in del_list:
        pepe.pop(elem)
    with open(f'{today}_log.json', 'w') as f:
        json.dump(pepe, f, indent=4)


def main():
    print('pivo')
    user_id = '123'
    floor = '1'
    mode = 'mode'
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    # print(type(time))
    finish_time1 = (datetime.datetime.now() +
                    datetime.timedelta(minutes=1)).strftime("%d-%m-%Y %H:%M")
    finish_time2 = (datetime.datetime.now() +
                    datetime.timedelta(minutes=2)).strftime("%d-%m-%Y %H:%M")
    progress = 'progress'
    write_to_json(user_id, floor, '1', mode,
                  time, finish_time1, progress)
    write_to_json(user_id, floor, '2', mode,
                  time, finish_time2, progress)

    delete_json()


if __name__ == '__main__':
    main()
