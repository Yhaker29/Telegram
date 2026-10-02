from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass
class user(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id:Mapped[int] = mapped_column(BigInteger)
    telegram_name:Mapped[str] = mapped_column(String)
    user_name: Mapped[str] = mapped_column(String,nullable=True)