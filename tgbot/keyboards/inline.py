from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import datetime
import json

floor_buttons = [
    [InlineKeyboardButton(callback_data='1', text='1')],
    [InlineKeyboardButton(callback_data='2', text='2')],
    [InlineKeyboardButton(callback_data='3', text='3')]
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


def create_rent_keyboard(mash_number, floor_number):
    rent_buttons = [[], [InlineKeyboardButton(
        text="Назад", callback_data="back")]]
    with open('active.json', 'r') as f:
        active = json.load(f)
    name = f'{floor_number}.{mash_number}'
    for i in range(1, 4):
        text = '🟢'
        cb = f'mash{i}'
        if active[name]['progress'] == True and active[name]['mash'] == cb:
            text = '🔴'
            cb = f'cancel{i}'
        rent_buttons[0].append(
            InlineKeyboardButton(callback_data=cb, text=text))
    rent_keyboard = InlineKeyboardMarkup(inline_keyboard=rent_buttons)
    return rent_keyboard
