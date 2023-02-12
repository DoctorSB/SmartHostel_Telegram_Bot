from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import State
from aiogram.types import Message


from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply("Вітаю, адміне!")


@admin_router.message(F.text == "ку")
async def user_ku(message: Message):
    await message.reply("Ку-ку")
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHL09ju_NYDBqyTq65N1BJqyacddxvSQACHxEAAowt_QcWMfHxvTZjli0E')
    await message.answer('Привет! Я чат-бот который поможет тебе не забыть о своих вещах ' + '🥰' + 'с чего начнем?')

#отправить стикер
# @admin_router.message(F.text == "стикер")
# async def user_sticker(message: Message):
