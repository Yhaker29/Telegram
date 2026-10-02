from sqlalchemy import select

from Databaze.models import user


async def add_user(session,telegram_id,user_name,telegram_name):
      new_user=user(telegram_id=telegram_id,telegram_name=telegram_name,user_name=user_name)
      session.add(new_user)
      await session.commit()
async def get_user(session,telegram_id):
    user1=select(user).where(user.telegram_id == telegram_id)
    result=await session.execute(user1)
    return result.scalar_one_or_none()

async def get_users(session):
    user1=select(user)
    result=await session.execute(user1)
    return result.scalars().all()