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
mode_keyboard= InlineKeyboardMarkup(inline_keyboard=mode_buttons)



async def create_keyboard():
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M")
    with open(f'{time}_log.json', 'r') as f:
        data = json.load(f)
    for key, value in data.items():
        if value['time'] != current_time:
            if value['car_number'] == 'mash1':
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(callback_data='mash1', text='🔴'),
                        InlineKeyboardButton(callback_data='mash2', text='🟢'),
                        InlineKeyboardButton(callback_data='mash3', text='🟢')
                    ],
                    [InlineKeyboardButton(text="Назад", callback_data="back")]
                ])
            elif value['car_number'] == 'mash2':
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(callback_data='mash1', text='🟢'),
                        InlineKeyboardButton(callback_data='mash2', text='🔴'),
                        InlineKeyboardButton(callback_data='mash3', text='🟢')
                    ],
                    [InlineKeyboardButton(text="Назад", callback_data="back")]
                ])

            elif value['car_number'] == 'mash3':
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(callback_data='mash1', text='🟢'),
                        InlineKeyboardButton(callback_data='mash2', text='🟢'),
                        InlineKeyboardButton(callback_data='mash3', text='🔴')
                    ],
                    [InlineKeyboardButton(text="Назад", callback_data="back")]
                ])
            return keyboard
