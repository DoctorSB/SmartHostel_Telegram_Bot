#создание машин состояний для каждого пользователя используя библиотеку aiogram3

from aiogram.fsm.state import State, StatesGroup

class Menu(StatesGroup):
    menu = State()
    sushechka = State()
    stiralka = State()
    floor = State()
    mode = State()
    in_progress = State()
    finish = State()
