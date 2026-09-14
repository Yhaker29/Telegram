from aiogram.utils.keyboard import ReplyKeyboardBuilder
from buttons_text import Buttons, admin_buttons


def home(admin_ID=None):
    keyboard = ReplyKeyboardBuilder()
    for btn in admin_buttons:
        if admin_ID==7077618482:

                # keyboard.button(text=btn, style="danger")
            keyboard.button(text=btn,style=admin_buttons[btn])
    keyboard.button(text='як справи?', style='primary')
    keyboard.button(text='дай наліпку')
    return keyboard.adjust(4).as_markup(resize_keyboard=True)
def start():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='thhfg')
    keyboard.button(text='gfgfgfrfff')
    keyboard.button(text='/command1')
    return keyboard.adjust(4).as_markup(resize_keyboard=True)
def як_справи():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='добре',style='success')
    keyboard.button(text='середнье', style='primary')
    keyboard.button(text='погано',style='danger')
    return keyboard.adjust(4).as_markup(resize_keyboard=True)
def наліпка():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Так',style='success')
    keyboard.button(text='Ні', style='danger')
    return keyboard.adjust(4).as_markup(resize_keyboard=True)