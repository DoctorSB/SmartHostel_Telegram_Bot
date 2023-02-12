from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton(callback_data='1', text='1')
button2 = InlineKeyboardButton(callback_data='2', text='2')
button3 = InlineKeyboardButton(callback_data='3', text='3')

markup = [[button1], [button2], [button3]]
keyboard = InlineKeyboardMarkup(inline_keyboard=markup)

stiralki = InlineKeyboardButton(callback_data='stiralka', text='Стиралки')
sushilki = InlineKeyboardButton(callback_data='sushilka', text='Сушилки')
instruc = InlineKeyboardButton(callback_data='instr', text='Инструкция')

menu_markup = [[stiralki], [sushilki], [instruc]]
menu_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_markup)

#inline клавиатура с 3 кнопками в одном ряду

mash1 = InlineKeyboardButton(callback_data='mash1', text='🟢')
mash2 = InlineKeyboardButton(callback_data='mash2', text='🟢')
mash3 = InlineKeyboardButton(callback_data='mash3', text='🟢')

#mash_keybord для их отображения

mash_markup = [[mash1], [mash2], [mash3]]
mash_keyboard = InlineKeyboardMarkup(inline_keyboard=mash_markup)

