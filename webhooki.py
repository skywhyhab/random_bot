import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_KEY = os.getenv('BOT_TOKEN')

if not API_KEY:
    exit("Token не найден")


WEBHOOT_HOST = 'https://6565-94-43-223-143.eu.ngrok.io'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOT_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 80

bot = Bot(token = API_KEY)
dp = Dispatcher(bot)

async def on_startup(dp):
    print('Starting...')
    await bot.set_webhook(WEBHOOK_URL)
    print('Webhook set!')

async def on_shutdown(dp):
    print('Sutting down...')
    await bot.delete_webhook()
    print('Webhook deleted')

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    return SendMessage(chat_id=msg.chat.id, text='Привет! Я бот!')

@dp.message_handler(commands=['help'])
async def help(msg: types.Message):
    return SendMessage(chat_id=msg.chat.id, text='Чем могу быть полезен?')

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=False,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )