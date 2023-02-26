from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
        InlineKeyboardButton(callback_data='mode1', text='100 мин'),
        InlineKeyboardButton(callback_data='mode2', text='90 мин'),
        InlineKeyboardButton(callback_data='mode3', text='95 мин')
    ],
    [
        InlineKeyboardButton(callback_data='mode4', text='80 мин'),
        InlineKeyboardButton(callback_data='mode5', text='30 мин'),
        InlineKeyboardButton(callback_data='mode6', text='230 мин')
    ],
    [
        InlineKeyboardButton(callback_data='mode7', text='125 мин'),
        InlineKeyboardButton(callback_data='mode8', text='125 мин'),
        InlineKeyboardButton(callback_data='mode9', text='220 мин')
    ],
    [
        InlineKeyboardButton(callback_data='mode10', text='125 мин'),
        InlineKeyboardButton(callback_data='mode11', text='50 мин'),
        InlineKeyboardButton(callback_data='mode12', text='100 мин')
    ],
    [
        InlineKeyboardButton(callback_data='mode13', text='65 мин'),
        InlineKeyboardButton(callback_data='mode14', text='135 мин'),
        InlineKeyboardButton(callback_data='mode15', text='50 мин')
    ],
    [
        InlineKeyboardButton(callback_data='mode16', text='10 мин'),
        InlineKeyboardButton(callback_data='mode17', text='3 мин')
    ],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
]
mode_keyboard = InlineKeyboardMarkup(inline_keyboard=mode_buttons)


def create_rent_keyboard(mash_number, floor_number):
    rent_buttons = [[], [InlineKeyboardButton(
        text="Назад", callback_data="back")]]
    with open('active.json', 'r') as f:
        active = json.load(f)
    keys = list(active.keys())
    name = f'{floor_number}.{mash_number}'
    for i in range(1, 4):
        text = '🟢'
        cb = f'mash{i}'
        for j in keys:
            if active[j]['progress'] == True and active[j]['floor'] == floor_number and active[j]['mash'] == cb:
                text = '🔴'
                cb = f'cancel{i}'
        if active[name]['progress'] == True and active[name]['mash'] == cb:
            text = '🔴'
            cb = f'cancel{i}'
        rent_buttons[0].append(
            InlineKeyboardButton(callback_data=cb, text=text))
    rent_keyboard = InlineKeyboardMarkup(inline_keyboard=rent_buttons)
    return rent_keyboard

sushilki_buttons = [
    [
        InlineKeyboardButton(callback_data='hours6', text='6 часов'),
        InlineKeyboardButton(callback_data='hours12', text='12 часов'),
        InlineKeyboardButton(callback_data='hours24', text='24 часа')
    ],
    [
        InlineKeyboardButton(callback_data='hours36', text='36 часов'),
        InlineKeyboardButton(callback_data='hours48', text='48 часов'),
        InlineKeyboardButton(callback_data='hours72', text='72 часа')
    ],
    [InlineKeyboardButton(text="Назад", callback_data="back")]
]
sushilki_keyboard = InlineKeyboardMarkup(inline_keyboard=sushilki_buttons)
