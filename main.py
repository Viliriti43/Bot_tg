import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
import os
from dotenv import load_dotenv
from gl_menu import set_commands
router = Router()
load_dotenv()

@router.message(Command(commands = ['start']))
async def start_command(messege: Message):
    await messege.answer("Привет")

@router.message()
async def otvet(massage:Message,bot:Bot):
    if massage.photo:
        file = await bot.get_file(massage.photo[-1].file_id)
        await massage.answer("Спасибо за кортинку")
        await bot.download_file(file.file_path,"photo.jpg")
    elif massage.sticker:
        await massage.answer("ненадо стикеры!")
    else:
        await massage.reply("Это текст")

async def start():
    API_Token = os.getenv("token")
    bot = Bot(API_Token)
    dp = Dispatcher()
    dp.include_router(router)
    await set_commands(bot)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(start())
