from aiogram import Router, F
from aiogram.types import Message
from tgbot.keyboards.inline import floor_keyboard, mode_keyboard, mash_keyboard, create_rent_keyboard
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram.filters.command import Command
from tgbot.users_logging.log import user_log
from tgbot.users_logging.logging import write_to_json
import datetime
from aiogram import Bot
from tgbot.config import load_config
from tgbot.misc import states


config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

user_router = Router()

logging_info = user_log()

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

def mode_chooshing(mode):
    return int(mode_dict[mode])


@user_router.message(Command('start'))
async def user_start(message: Message, state: FSMContext):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах. Выбери этаж.', reply_markup=floor_keyboard)
    logging_info.id = message.from_user.id

#-------------------------------- ВЫБОР ЭТАЖА ---------------------------------------------
# обработка inline кнопок и изменение текста кнопки
@user_router.callback_query(F.data == '1')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    try:
        await query.message.edit_reply_markup(reply_markup=create_rent_keyboard(logging_info.mash, logging_info.floor))
    except:
        await query.message.edit_reply_markup(reply_markup=mash_keyboard)
        print(logging_info.mash, logging_info.floor)


@user_router.callback_query(F.data == '2')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    try:
        await query.message.edit_reply_markup(reply_markup=create_rent_keyboard(logging_info.mash, logging_info.floor))
    except:
        await query.message.edit_reply_markup(reply_markup=mash_keyboard)


@user_router.callback_query(F.data == '3')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери стиральную машинку')
    logging_info.floor = query.data
    try:
        await query.message.edit_reply_markup(reply_markup=create_rent_keyboard(logging_info.mash, logging_info.floor))
    except:
        await query.message.edit_reply_markup(reply_markup=mash_keyboard)


#-------------------------------- ВЫБОР СТИРАЛЬНОЙ МАШИНКИ --------------------------------
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


#-------------------------------- ВЫБОР РЕЖИМА СТИРКИ -------------------------------------
@user_router.callback_query(F.data.in_(mode_dict))
async def user_callback1(query, state: FSMContext):
    time = datetime.datetime.now()
    delta = datetime.datetime.now() + datetime.timedelta(minutes=mode_chooshing(query.data))
    print(mode_chooshing(query.data))
    logging_info.mode = query.data
    logging_info.time = time.strftime("%d-%m-%Y %H:%M")
    logging_info.finish_time = delta.strftime("%d-%m-%Y %H:%M")
    logging_info.progress = True
    write_to_json(logging_info.id, logging_info.floor,
                  logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress)
    await query.message.edit_text('В процессе')
    while time.strftime("%d-%m-%Y %H:%M") < logging_info.finish_time:
        await asyncio.sleep(60)
        time = datetime.datetime.now()
        if time.strftime("%d-%m-%Y %H:%M") == delta.strftime("%d-%m-%Y %H:%M"):
            await query.message.answer('Осталось менее 5 минут')
    logging_info.progress = False
    write_to_json(logging_info.id, logging_info.floor,
                  logging_info.mash, logging_info.mode, logging_info.time, logging_info.finish_time, logging_info.progress)
    await query.message.edit_text('Твое белье уже ждет тебя!')





@user_router.callback_query(F.data == 'back')
async def user_callback1(query, state: FSMContext):
    await query.message.edit_text('Выбери этаж', reply_markup=floor_keyboard)
