"""Telegram."""

from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from dependency_injector.wiring import Provide, inject


@inject
async def tg_polling(
    dp: Dispatcher = Provide['dp'],
    bot: Bot = Provide['bot'],
    config: dict = Provide['config'],
):

    def is_user_correct(message: Message):
        return str(message.from_user.id) in config["app"]["admins"]

    @dp.message(CommandStart())
    async def command_start_handler(message: Message):
        """Handler for the `/start` command."""
        if not is_user_correct(message):
            await message.answer(f'i don`t know who you are, sorry, buy')
            return

        await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')

    @dp.message()
    async def get_message(message: Message):
        if not is_user_correct(message):
            await message.answer(f'i don`t know who you are, sorry, buy')
            return

        ...

    await dp.start_polling(bot)
