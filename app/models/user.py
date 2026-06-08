import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import Enum as SAEnum, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from app.models.enums import Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[Role] = mapped_column(SAEnum(Role), default=Role.viewer)
    created_at: Mapped[Optional[datetime]] = mapped_column(server_default=func.now())
