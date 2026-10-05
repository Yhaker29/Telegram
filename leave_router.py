from aiogram import Router, Bot
from aiogram.filters import (
    ChatMemberUpdatedFilter,
    IS_NOT_MEMBER,
    IS_MEMBER,
    JOIN_TRANSITION,
)
from aiogram.types import ChatMemberUpdated

from config import settings

leave_router = Router()
@leave_router.my_chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def on_user_leave(event: ChatMemberUpdated, bot: Bot):
    await bot.send_message(chat_id=settings.ADMIN_ID,text=f'Користувач {event.from_user.full_name} заблокував бот ⛔')

@leave_router.my_chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def on_user_join(event: ChatMemberUpdated, bot: Bot):
    await bot.send_message(chat_id=settings.ADMIN_ID, text=f'Користувач {event.from_user.full_name} розблокував бот ✅')