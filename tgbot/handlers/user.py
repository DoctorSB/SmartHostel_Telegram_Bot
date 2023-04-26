from aiogram import Router, F
from aiogram.types import Message
from tgbot.keyboards.inline import floor_keyboard, mode_keyboard, mash_keyboard, create_rent_keyboard, sushilki_keyboard
from tgbot.keyboards.reply import restart_keyboard
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram.filters.command import Command
from tgbot.models.log import Log
from tgbot.models.logging import write_to_json
import datetime
from aiogram import Bot
from tgbot.config import load_config
from tgbot.misc import states
from aiogram.types import ReplyKeyboardRemove


config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

user_router = Router()

logging_info = Log()

sush_time = {
    'hours6': '360',
    'hours12': '720',
    'hours24': '1440',
    'hours36': '2160',
    'hours48': '2880',
    'hours72': '4320',
}


mode_dict = {
    'mode1': '100',
    'mode2': '90',
    'mode3': '95',
    'mode4': '80',
    'mode5': '30',
    'mode6': '230',
    'mode7': '125',
    'mode8': '125',
    'mode9': '220',
    'mode10': '125',
    'mode11': '50',
    'mode12': '100',
    'mode13': '65',
    'mode14': '135',
    'mode15': '50',
    'mode16': '10',
    'mode17': '3',
}

floor_numbers = ['1', '2', '3']

mash_numbers = ['mash1', 'mash2', 'mash3']


def sush_time_choosing(time):
    return int(sush_time[time])


def mode_chooshing(mode):
    return int(mode_dict[mode])


@user_router.message(Command('start'))
async def user_start(message: Message, state: FSMContext):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах. Выбери этаж.', reply_markup=floor_keyboard)
    logging_info.id = message.from_user.id

# -------------------------------- ВЫБОР ЭТАЖА ---------------------------------------------
# обработка inline кнопок и изменение текста кнопки


@user_router.callback_query(F.data.in_(floor_numbers))
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    try:
        await query.message.edit_reply_markup(reply_markup=create_rent_keyboard(logging_info.mash, logging_info.floor))
    except:
        await query.message.edit_reply_markup(reply_markup=mash_keyboard)
        print(logging_info.mash, logging_info.floor)


# -------------------------------- ВЫБОР СТИРАЛЬНОЙ МАШИНКИ --------------------------------
@user_router.callback_query(F.data.in_(mash_numbers))
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mash = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)


# -------------------------------- ВЫБОР РЕЖИМА СТИРКИ -------------------------------------
@user_router.callback_query(F.data.in_(mode_dict))
async def user_callback1(query, state: FSMContext):
    ht = 0
    time = datetime.datetime.now()
    finish = datetime.datetime.now() + datetime.timedelta(minutes=mode_chooshing(query.data))
    five_minutes = finish - datetime.timedelta(minutes=5)
    logging_info.mode = query.data
    logging_info.time = time.strftime("%d-%m-%Y %H:%M")
    logging_info.finish_time = finish.strftime("%d-%m-%Y %H:%M")
    logging_info.progress = True
    write_to_json(logging_info.id, logging_info.floor, logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress, logging_info.sushu)
    await query.message.edit_text('В процессе')
    while time.strftime("%d-%m-%Y %H:%M") < logging_info.finish_time:
        time = datetime.datetime.now()
        if time.strftime("%d-%m-%Y %H:%M") >= five_minutes.strftime("%d-%m-%Y %H:%M") and ht == 0:
            ht = 1
            await query.message.reply('Через 5 минут твое белье будет готово!')
        await asyncio.sleep(30)
    logging_info.progress = False
    write_to_json(logging_info.id, logging_info.floor,
                  logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress, logging_info.sushu)
    await query.message.answer('Твое белье уже ждет тебя!', reply_markup=restart_keyboard)


# -------------------------------- КНОПКА НАЗАД --------------------------------------------
@user_router.callback_query(F.data == 'back')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери этаж', reply_markup=floor_keyboard)


# -------------------------------- КНОПКА ПЕРЕЗАПУСКА --------------------------------------
@user_router.message(F.text == 'Перезапустить')
async def user_message(message: Message, state: FSMContext):
    await message.answer('Нажми /start', reply_markup=ReplyKeyboardRemove())


# -------------------------------- КНОПКА СУШИЛКИ --------------------------------------
@user_router.message(F.text == 'Ставлю на сушилку')
async def user_message(message: Message, state: FSMContext):
    await message.answer_sticker('CAACAgIAAxkBAAEH6Dtj-rYSMaJNEoO91OTfUItpj2SyLwACtBMAAmPqyEs25hl-KD1TMS4E', reply_markup=ReplyKeyboardRemove())
    await message.answer('Выбери время', reply_markup=sushilki_keyboard)


@user_router.callback_query(F.data.in_(sush_time))
async def user_callback1(query, state: FSMContext):
    ht = 0
    time = datetime.datetime.now()
    finish = datetime.datetime.now(
    ) + datetime.timedelta(minutes=sush_time_choosing(query.data))
    five_minutes = finish - datetime.timedelta(minutes=30)
    logging_info.time = time.strftime("%d-%m-%Y %H:%M")
    logging_info.finish_time = finish.strftime("%d-%m-%Y %H:%M")
    logging_info.sushu = True
    write_to_json(logging_info.id, logging_info.floor,
                  logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress, logging_info.sushu)
    await query.message.edit_text('Сушусь')
    while time.strftime("%d-%m-%Y %H:%M") < logging_info.finish_time:
        time = datetime.datetime.now()
        if time.strftime("%d-%m-%Y %H:%M") >= five_minutes.strftime("%d-%m-%Y %H:%M") and ht == 0:
            ht = 1
            await query.message.reply('Через 30 минут твое белье будет готово!')
        await asyncio.sleep(600)
    logging_info.sushu = False
    write_to_json(logging_info.id, logging_info.floor,
                  logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress, logging_info.sushu)
    await query.message.answer('Твое белье уже ждет тебя!', reply_markup=restart_keyboard)
