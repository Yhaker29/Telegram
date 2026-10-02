
from Databaze.models import user


async def add_user(session,telegram_id,user_name,telegram_name):
      new_user=user(telegram_id=telegram_id,telegram_name=telegram_name,user_name=user_name)
      session.add(new_user)
      await session.commit()