import json
from aiogram.fsm.context import FSMContext
from random import random
import random
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import F

from keyboards import home, наліпка

media_router = Router()

@media_router.message(F.sticker,F.from_user.id==7077618482  )
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
async def sticker(message: Message):
    await message.answer(text='Чи впевнені ви що хочите додати цю наліпку?', reply_markup=наліпка())
    await state.update_data(sticker_id=sticker_id)
@media_router.message(F.text=='Так')
async def text(message: Message):
    await message.answer(text='Заявка відправлена адміну',reply_markup=home(message.from_user.id==7077618482))