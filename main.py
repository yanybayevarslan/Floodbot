from aiogram import types, F, Dispatcher, Bot
from aiogram.filters import Command
import os
import asyncio
import loguru

CHAT_ID = "@okak_group"
bot = Bot("8534936381:AAE26tUXl8vfsZiftgBTBKwGDGbRhtrL-9Y")
dp = Dispatcher()

@dp.message(Command("send"))
async def flood_message(message: types.Message, chat_id=CHAT_ID,Bot=bot):
    a = message.text.split(maxsplit=2)

    if len(a) < 3:
        return message.answer("usage: /send [times-loop] [text]")

    count = int(a[1])
    text = str(a[2])

    try:
        while 0 < count:
            await bot.send_message(chat_id,text=text)
            count+=1
            await asyncio.sleep(0.05)

        await message.answer("✅COMPELETED")
    except Exception as e:
        logger.error(f"LIMIT ERROR{e}")

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Hello welcome to the bot!")

async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    print("BOT RUNNING...")
    asyncio.run(main())
