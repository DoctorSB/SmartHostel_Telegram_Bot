from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import types, Router, F


user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вітаю, звичайний користувач!")
    user_router.next()

@user_router.message(F.text == "ку")
async def user_ku(message: Message):
    await message.reply("Ку-ку")