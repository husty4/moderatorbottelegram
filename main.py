# -*- coding utf8 -*-
import logging
from aiogram import Bot, Dispatcher, executor, types

import config


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(content_types=["new_chat_members"])
async def user_joined(message: types.Message):
    await message.answer("Hello, man")

@dp.message_handler()
async def msg_handler(message: types.Message):
    text = message.text.lower()
    for word in config.words:
        if word in text:
            await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)