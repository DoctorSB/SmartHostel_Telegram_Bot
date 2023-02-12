from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from tgbot.keyboards.inline import keyboard, menu_keyboard, mash_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах ' + '🥰' + 'с чего начнем?')

@user_router.message(F.text == "Меню")
async def user_ku(message: Message):
    await message.answer('Выбери раздел который тебя интересует', reply_markup=menu_keyboard)

@user_router.callback_query(F.data == 'stiralka')
async def user_callback1(query):
    await query.message.edit_text('Выбери этаж')
    await query.message.edit_reply_markup(reply_markup=keyboard)


@user_router.message(F.text == "Инструкция")
async def user_hello(message: Message):
    await message.answer('тут будет инструкция', reply_markup=keyboard)


#обработка inline кнопок и изменение текста кнопки
@user_router.callback_query(F.data == '1')
async def user_callback1(query):
    await query.message.edit_text('выбери машинку')
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)



