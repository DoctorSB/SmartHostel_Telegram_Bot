from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

restart_button = [
    [KeyboardButton(text="Перезапустить")],
    [KeyboardButton(text="Ставлю на сушилку")]
]

restart_keyboard = ReplyKeyboardMarkup(keyboard=restart_button, resize_keyboard=True,
                                       one_time_keyboard=True, input_field_placeholder='Выбери следующий шаг')
