#создание машин состояний для каждого пользователя используя библиотеку aiogram3

from aiogram.fsm.state import State, StatesGroup

class User(StatesGroup):
    floor = State()
    mash = State()
    mode = State()
    progress = State()

