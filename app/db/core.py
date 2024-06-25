"""Модуль содержит классы для работы с базой данных."""
import asyncio

from aiogram.types import Chat
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from models.base import session_factory
from models.models import Users


async def insert_user(
        user_id: int,
        username: str,
        first_name: str,
        last_name: str,
        chat: Chat
) -> None:
    """
    Добавление пользователя в базу данных
    :param user_id: id пользователя
    :param username: имя пользователя
    :param first_name: имя
    :param last_name: фамилия
    :param chat: Объект чата
    """
    stmt_user = (
        insert(Users).values(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name
        )).on_conflict_do_nothing(
            index_elements=["user_id"]
    )

    current_session = await session_factory()
    async with current_session() as session:
        await session.execute(stmt_user)
        await session.commit()


async def check_registry_user(
        user_id: int,
        group_chat_id: int
) -> bool:
    """Проверка наличия пользователя в базе данных."""
    current_session = await session_factory()
    async with current_session() as session:
        query = (
            select(Users.user_id).
            select_from(Users).
            where(Users.user_id == user_id)
        )

        result = await session.execute(query)
        return bool(result.scalar())


if __name__ == "__main__":
    asyncio.run(
            insert_user(
                    177,
                    "test",
                    "test",
                    "test",
                    7
            )
    )
