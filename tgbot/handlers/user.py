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


def mode_choosing(mode):
    return int(mode_dict[mode])


def update_logging_info(query, logging_info, finish):
    logging_info.mode = query.data
    logging_info.time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    logging_info.finish_time = finish.strftime("%d-%m-%Y %H:%M")
    logging_info.progress = True
    return logging_info


def update_sushu_logging_info(logging_info, finish):
    logging_info.time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    logging_info.finish_time = finish.strftime("%d-%m-%Y %H:%M")
    logging_info.sushu = True
    return logging_info



async def countdown(query, finish_time):
    ht = 0
    finish_time_new = datetime.datetime.strptime(finish_time, "%d-%m-%Y %H:%M")
    # five_minutes is now a datetime object
    five_minutes = finish_time_new - datetime.timedelta(minutes=5)
    
    while datetime.datetime.now() < finish_time_new:
        time = datetime.datetime.now()
        if time >= five_minutes and ht == 0:
            ht = 1
            await query.message.reply('Через 5 минут твое белье будет готово!')
        await asyncio.sleep(30)

async def sushu_countdown(query, finish_time):
    time = datetime.datetime.now()
    finish_time_new = datetime.datetime.strptime(finish_time, "%d-%m-%Y %H:%M")
    ht = 0
    thirty_minutes = finish_time_new - datetime.timedelta(minutes=30)
    while time.strftime("%d-%m-%Y %H:%M") < finish_time:
        time = datetime.datetime.now()
        if time.strftime("%d-%m-%Y %H:%M") >= thirty_minutes.strftime("%d-%m-%Y %H:%M") and ht == 0:
            ht = 1
            await query.message.reply('Через 30 минут твое белье будет готово!')
        await asyncio.sleep(600)


@user_router.message(Command('start'))
async def user_start(message: Message, state: FSMContext):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах. Выбери этаж.', reply_markup=floor_keyboard)
    logging_info.id = message.from_user.id


@user_router.callback_query(F.data.in_(floor_numbers))
async def floor_selection_callback(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    try:
        await query.message.edit_reply_markup(reply_markup=create_rent_keyboard(logging_info.mash, logging_info.floor))
    except:
        await query.message.edit_reply_markup(reply_markup=mash_keyboard)


# -------------------------------- ВЫБОР СТИРАЛЬНОЙ МАШИНКИ --------------------------------
@user_router.callback_query(F.data.in_(mash_numbers))
async def сhoose_washing_mode(query, state: FSMContext):
    await query.message.edit_text('Выбери режим стирки')
    logging_info.mash = query.data
    await query.message.edit_reply_markup(reply_markup=mode_keyboard)


# -------------------------------- ВЫБОР РЕЖИМА СТИРКИ -------------------------------------
@user_router.callback_query(F.data.in_(mode_dict))
async def log_in_json(query, state: FSMContext):
    finish = datetime.datetime.now() + datetime.timedelta(minutes=mode_choosing(query.data))
    logging_info_new = update_logging_info(query, logging_info, finish)
    write_to_json(logging_info_new)
    await query.message.edit_text('В процессе')
    await countdown(query, logging_info_new.finish_time)
    logging_info_new.progress = False
    write_to_json(logging_info_new)
    await query.message.answer('Твое белье уже ждет тебя!', reply_markup=restart_keyboard)


# -------------------------------- КНОПКА НАЗАД --------------------------------------------
@user_router.callback_query(F.data == 'back')
async def cancel(query, state: FSMContext):
    await query.message.edit_text('Выбери этаж', reply_markup=floor_keyboard)


# -------------------------------- КНОПКА ПЕРЕЗАПУСКА --------------------------------------
@user_router.message(F.text == 'Перезапустить')
async def restart(message: Message, state: FSMContext):
    await message.answer('Нажми /start', reply_markup=ReplyKeyboardRemove())


# -------------------------------- КНОПКА СУШИЛКИ --------------------------------------
@user_router.message(F.text == 'Ставлю на сушилку')
async def put_on_sushilka(message: Message, state: FSMContext):
    await message.answer_sticker('CAACAgIAAxkBAAEH6Dtj-rYSMaJNEoO91OTfUItpj2SyLwACtBMAAmPqyEs25hl-KD1TMS4E', reply_markup=ReplyKeyboardRemove())
    await message.answer('Выбери время', reply_markup=sushilki_keyboard)


@user_router.callback_query(F.data.in_(sush_time))
async def user_callback1(query, state: FSMContext):
    finish = datetime.datetime.now(
    ) + datetime.timedelta(minutes=sush_time_choosing(query.data))
    logging_info_new = update_sushu_logging_info(logging_info, finish)
    write_to_json(logging_info_new)
    await query.message.edit_text('Сушусь')
    await sushu_countdown(query, logging_info_new.finish_time)
    logging_info_new.sushu = False
    write_to_json(logging_info_new)
    await query.message.answer('Твое белье уже ждет тебя!', reply_markup=restart_keyboard)
