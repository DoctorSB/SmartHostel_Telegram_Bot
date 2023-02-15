from aiogram import Router, F
from aiogram.types import Message
from tgbot.keyboards.inline import floor_keyboard, mode_keyboard, mash_keyboard, create_keyboard
from tgbot.misc.states import Menu
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram.filters.command import Command
from tgbot.users_logging.log import user_log
from tgbot.users_logging.logging import write_to_json, check_file
import datetime


user_router = Router()

logging_info = user_log()


@user_router.message(Command('start'))
async def user_start(message: Message, state: FSMContext):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах. Выбери этаж.', reply_markup=floor_keyboard)
    await check_file()
    logging_info.id = message.from_user.id
    logging_info.floor = None
    logging_info.mode = None
    logging_info.time = None
    logging_info.mash = None
    logging_info.finish_time = None
    logging_info.progress = False


# обработка inline кнопок и изменение текста кнопки
@user_router.callback_query(F.data == '1')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)


@user_router.callback_query(F.data == '2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)


@user_router.callback_query(F.data == '3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    await query.message.edit_reply_markup(reply_markup=mash_keyboard)


@user_router.callback_query(F.data == 'mash1')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mash = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)


@user_router.callback_query(F.data == 'mash2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mash = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)


@user_router.callback_query(F.data == 'mash3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mash = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)


@user_router.callback_query(F.data == 'mode1')
async def user_callback1(query, state: FSMContext):
    time = datetime.datetime.now()
    logging_info.mode = query.data
    logging_info.time = time.strftime("%d-%m-%Y %H:%M")
    logging_info.finish_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    logging_info.progress = True
    await state.set_state(Menu.in_progress)
    write_to_json(logging_info.id, logging_info.floor,
                  logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress)
    await create_keyboard()
    await query.message.edit_text('В процессе')
    await asyncio.sleep(20)
    logging_info.progress = False
    write_to_json(logging_info.id, logging_info.floor,
                    logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress)
    await create_keyboard()
    await query.message.edit_text('Твое белье уже ждет тебя!')
    await state.set_state(Menu.finish)


@user_router.callback_query(F.data == 'mode2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mode = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)
    await state.set_state(Menu.in_progress)
    await asyncio.sleep(2700)
    await query.message.edit_text('Твое белье уже ждет тебя!')
    await state.set_state(Menu.finish)


@user_router.callback_query(F.data == 'mode3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mode = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)
    await state.set_state(Menu.in_progress)
    await asyncio.sleep(3600)
    await query.message.edit_text('Твое белье уже ждет тебя!')
    await state.set_state(Menu.finish)

# отправить сообщение о завершении


@user_router.callback_query(F.data == 'back')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери этаж', reply_markup=floor_keyboard)
    logging_info.floor = None
    logging_info.mode = None
    logging_info.time = None
    logging_info.mash = None
    logging_info.finish_time = None
    logging_info.progress = False
    await state.set_state(Menu.start)

