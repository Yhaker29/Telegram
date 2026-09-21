import json
from aiogram.fsm.context import FSMContext
from random import random
import random
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import F

from config import settings
from keyboards import home, наліпка
from state import Menu

media_router = Router()

@media_router.message(F.sticker,F.from_user.id==settings.ADMIN_ID  )
async def sticker(message: Message):
    await message.answer(text=f"Дякую за наліпочку")
    await message.answer_sticker(sticker=message.sticker.file_id)
    print(message.sticker.file_id)
    with open("sticker.json", 'r') as file:
        b= json.load(file)
        b.append(message.sticker.file_id)
    with open("sticker.json", 'w') as file:
        json.dump(b, file,indent=4)
@media_router.message(F.text=='дай наліпку')
async def text(message: Message):
    with open("sticker.json", 'r') as file:
        b= json.load(file)
    await message.answer_sticker(sticker=random.choice(b))
@media_router.message(F.sticker)
async def sticker(message: Message,state: FSMContext):
    sticker_id = message.sticker.file_id
    await message.answer(text='Чи впевнені ви що хочите додати цю наліпку?', reply_markup=наліпка())
    await state.update_data(sticker_id=sticker_id)
    # {"sticker_id":"qwertyhjfdsz"}


@media_router.message(F.text == 'Так',Menu.mood,F.from_user.id==settings.ADMIN_ID)
async def mood(message: Message,state: FSMContext):
    pass

@media_router.message(F.text=='Так')
async def text(message: Message,state: FSMContext):
    data = await state.get_data()
    sticker_id = data.get('sticker_id')
    msg=await message.bot.send_sticker(sticker=sticker_id,chat_id=7077618482)
    await message.bot.send_message(chat_id=7077618482,text=f'Цю наліпку відправив {message.from_user.full_name} '
                                   ,reply_to_message_id=msg.message_id, reply_markup=наліпка())
    await state.set_state(Menu.mood)
    await message.answer(text='Заявка відправлена адміну',reply_markup=home(message.from_user.id==7077618482))