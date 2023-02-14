#создать класс для логирования

import json
import datetime
import os
from tgbot.users_logging.logging import create_new_json

class user_log():
    def __init__(self, user_id=0, floor=0, mash='', mode='', time=''):
        self.id = user_id
        self.floor = floor
        self.mash = mash
        self.mode = mode
        self.time = time

    def write_to_json(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(f'{today}_log.json', 'r') as f:
            data = json.load(f)
        data[self.user_id] = {'floor': self.floor, 'car_number': self.car_number, 'mode': self.mode, 'time': self.time}
        with open(f'{today}_log.json', 'w') as f:
            json.dump(data, f)
    
    def read_from_json(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(f'{today}_log.json', 'r') as f:
            data = json.load(f)
        return data[self.user_id]

    def check_file(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        if f'{today}_log.json' not in os.listdir():
            create_new_json()
        else:
            pass