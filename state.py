from aiogram.fsm.state import State,StatesGroup
class Menu(StatesGroup):
    message_state =State()
    home=State()
    sticker=State()
    mood=State()
    all_rosilka=State()
    message=State()