from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from tgbot.keyboards.inline import floor_keyboard, menu_keyboard, mash_keyboard, mode_keyboard
from tgbot.misc.states import Menu
from aiogram.fsm.context import FSMContext
import asyncio

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах ' + '🥰' + 'с чего начнем?')


@user_router.message(F.text == "Меню")
async def user_ku(message: Message, state: FSMContext):
    await message.answer('Выбери раздел который тебя интересует', reply_markup=menu_keyboard)
    await state.set_state(Menu.menu)


@user_router.callback_query(F.data == 'stiralka')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери этаж')
    await query.message.edit_reply_markup(reply_markup=floor_keyboard)
    await state.set_state(Menu.stiralka)


@user_router.callback_query(F.data == 'sushilka')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери этаж')
    await query.message.edit_reply_markup(reply_markup=floor_keyboard)
    await state.set_state(Menu.sushechka)

@user_router.message(F.text == "Инструкция")
async def user_hello(message: Message, state: FSMContext):
    await message.answer('тут будет инструкция', reply_markup=mash_keyboard)
    await state.set_state(Menu.instr)


# обработка inline кнопок и изменение текста кнопки
@user_router.callback_query(F.data == '1')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери машинку')
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)



@user_router.callback_query(F.data == '2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери машинку')
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)

@user_router.callback_query(F.data == '3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери машинку')
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)

@user_router.callback_query(F.data == 'mash1')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери режим')
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)

@user_router.callback_query(F.data == 'mash2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери режим')
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)

@user_router.callback_query(F.data == 'mash3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери режим')
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)

@user_router.callback_query(F.data == 'mode1')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери режим')
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)

@user_router.callback_query(F.data == 'mode2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери режим')
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)

@user_router.callback_query(F.data == 'mode3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('выбери режим')
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)
    await state.set_state(Menu.in_progress)
    #установить таймер на 30 минут
    #после 30 минут отправить сообщение о завершении
    time = 30
    await asyncio.sleep(time)
    await query.message.edit_text('Ваша машинка готова')
    #отправить сообщение о завершении
    await state.set_state(Menu.finish)

#отправить сообщение о завершении

@user_router.callback_query(F.data == 'back')
async def user_callback1(query, state: FSMContext):
    pass