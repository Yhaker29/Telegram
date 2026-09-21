import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.utils import keyboard
from buttons_text import Buttons
from handlers.media_handler import media_router
from keyboards import home, start, як_справи
from state import Menu
from config import settings

TOKEN = settings.TOKEN
dp = Dispatcher()
dp.include_router(media_router)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=f"Привіт, {html.bold(message.from_user.full_name)}!", reply_markup=start()
    )


@dp.message(F.text == "/command1")
async def echo_handler(message: Message, state) -> None:
    await message.answer(text="1", reply_markup=home(message.from_user.id))


@dp.message(F.photo)
async def photo_handler(message: Message) -> None:
    await message.answer(text=f"Що?")


@dp.message(F.text.lower().contains(Buttons.hello), F.from_user.id == 7077618482)
async def echo_handler(message: Message) -> None:
    await message.answer(text=f"Привіт господару")


@dp.message(F.text.lower() == Buttons.goodbye, F.from_user.id == 7077618482)
async def echo_handler(message: Message) -> None:
    await message.answer(text=f"пака господару")


@dp.message(F.voice)
async def photo_handler(message: Message) -> None:
    await message.answer(text=f"Що?")


@dp.message(F.text == "добрий день")
async def echo_handler(message: Message) -> None:
    await message.answer(text=f"допобачення")


@dp.message(F.text == "hello")
async def echo_handler(message: Message) -> None:
    await message.answer(text=f"Goodbye")


@dp.message(F.text == "goodbye")
async def echo_handler(message: Message) -> None:
    await message.answer(text=f"hello")


@dp.message(F.text == "як справи?")
async def echo_handler(message: Message, state) -> None:
    await message.answer(text=f"обери", reply_markup=як_справи())


@dp.message(F.text == "погано")
async def echo_handler(message: Message, state) -> None:
    await message.answer(text=f"що сталося?", reply_markup=home(message.from_user.id))


@dp.message(F.text == "середнье")
async def echo_handler(message: Message, state) -> None:
    await message.answer(text=f"це добре!", reply_markup=home(message.from_user.id))


@dp.message(F.text == Buttons.roblox)
async def echo_handler(message: Message) -> None:
    await message.answer(
        text=f"РОООООООООООООООООООООООООООООООООООООООООООООООООООООООБЛОКС!!!!!!!",
        reply_markup=home(message.from_user.id),
    )
    await message.answer_sticker(
        sticker=(
            "CAACAgIAAxkBAAIPHGqQPHqdpiJSXXliRrLJ7VoqawWZAALohwACozrASKe8I-gTzQHwPQQ"
        )
    )


@dp.message(F.text == "добре")
async def echo_handler(message: Message, state) -> None:
    await message.answer(text=f"класно!", reply_markup=home(message.from_user.id))


@dp.message(F.text == "Дай фото")
async def echo_handler(message: Message) -> None:
    dx = await message.answer_photo(
        photo=FSInputFile(r"C:\Users\Yahakerr\Downloads\Ukraine.jpg")
    )
    print(dx.photo[-1].file_id)
    await message.answer_photo(
        photo="AgACAgIAAxkDAAIcaGqtZSnoF03mMvtrVgwHdS_G7o1sAAJwH2sbnPhxSZWdcdX7C2K7AQADAgADeAADPQQ"
    )
    # await message.answer_photo(photo
    #     ='https://static.ukrinform.com/photos/2022_12/thumb_files/630_360_1671628705-480.jpeg',
    #         caption='Слава Україні',show_caption_above_media=True)


# @dp.message()
# async def echo_handler(message: Message) -> None:
#         await message.send_copy(chat_id=message.chat.id)
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
