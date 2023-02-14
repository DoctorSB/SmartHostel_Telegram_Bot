from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu_buttons = [

        [InlineKeyboardButton(callback_data='stiralka', text='Стиралки')],
        [InlineKeyboardButton(callback_data='sushilka', text='Сушилки')],
        [InlineKeyboardButton(callback_data='instr', text='Инструкция')]
]
menu_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_buttons)

floor_buttons = [
    [
        InlineKeyboardButton(callback_data='1', text='1'),
        InlineKeyboardButton(callback_data='2', text='2'),
        InlineKeyboardButton(callback_data='3', text='3')
    ],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
]
floor_keyboard = InlineKeyboardMarkup(inline_keyboard=floor_buttons)

mash_buttons = [
    [
        InlineKeyboardButton(callback_data='mash1', text='🟢'),
        InlineKeyboardButton(callback_data='mash2', text='🟢'),
        InlineKeyboardButton(callback_data='mash3', text='🟢')
    ],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
]
mash_keyboard = InlineKeyboardMarkup(inline_keyboard=mash_buttons)

mode_buttons = [
    [
        InlineKeyboardButton(callback_data='mode1', text='30 мин'),
        InlineKeyboardButton(callback_data='mode2', text='45 мин'),
        InlineKeyboardButton(callback_data='mode3', text='1 час')
    ],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
]
mode_keyboard = InlineKeyboardMarkup(inline_keyboard=mode_buttons)