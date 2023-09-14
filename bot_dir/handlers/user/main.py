from aiogram import Dispatcher
from aiogram.types import Message
from database.methods import get


async def start(message: Message):
    try:
        table_lst = get.select_tables()
        print(table_lst)
    except:
        await message.bot.send_message(message.chat.id, 'smth wrong')
    await message.reply('message to start')


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=['start'])
