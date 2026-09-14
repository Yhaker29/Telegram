from aiogram.fsm.state import State,StatesGroup
class Menu(StatesGroup):
    home=State()
    sticker=State()
    mood=State()