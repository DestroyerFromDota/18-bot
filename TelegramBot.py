from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from connect_mySQL import *

import random


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = ''

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Sexbot!\nНапиши мне что-нибудь\n'
                         'для подсказок пиши /help')

@dp.message(Command(commands=["place"]))
async def process_start_command(message: Message):
    await message.answer(random.choice(['kitchen', 'bathroom', 'bedroom', 'armchair']))

@dp.message(Command(commands=["sex"]))
async def process_start_command(message: Message):
    await message.answer(random.choice(['anal sex', 'oral sex', 'vaginal sex']))

@dp.message(Command(commands=["role"]))
async def process_start_command(message: Message):
    with open('role.txt') as f:
        role = random.choice([i for i in f])
    await message.answer((role))

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Привет)\n'
                         'Пиши /sex для выбора вида секса\n'
                         'Для выбора места напиши /place\n'
                         'Для выбора ролей напиши /role')

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.reply(text=f'{select_conn_answerDB(message.text.lower())}')
        print(message)
        print(message.text)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)
