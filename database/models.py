from sqlalchemy import Text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    data: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
class Post(Base):
    __tablename__ = 'post'

    message_id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    publication_date: Mapped[datetime]
