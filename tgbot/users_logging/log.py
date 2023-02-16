# создать класс для логирования

import json
import datetime
import os
from tgbot.users_logging.logging import create_new_json


class user_log():
    def __init__(self, user_id=0, floor=0, mash='', mode='', time='', finish_time='', progress=False):
        self.id = user_id
        self.floor = floor
        self.mash = mash
        self.mode = mode
        self.time = time
        self.finish_time = finish_time
        self.progress = progress


