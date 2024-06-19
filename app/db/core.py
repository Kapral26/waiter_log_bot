"""Модуль содержит классы для работы с базой данных."""
import asyncio
from collections.abc import Sequence
from typing import Any

from aiogram.types import Chat
from sqlalchemy import URL, select, and_, func, Row
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession

from config.config_reader import Settings
from utils.db.models import Users, FoundErrors, UsersGroups, Groups


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

    stmt_group = (
        insert(Groups).values(
                name=chat.title,
                group_id=chat.id
        )).on_conflict_do_nothing(index_elements=["group_id"])

    stmt_users_group = (
        insert(UsersGroups).values(
                user_id=user_id,
                group_id=chat.id
        )).on_conflict_do_nothing(
            index_elements=["user_id", "group_id"]
    )

    current_session = await session_factory()
    async with current_session() as session:
        for stmt in (stmt_user, stmt_group, stmt_users_group):
            await session.execute(stmt)
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
            join(UsersGroups, UsersGroups.user_id == Users.user_id).
            where(and_(Users.user_id == user_id, UsersGroups.group_id == group_chat_id))
        )

        result = await session.execute(query)
        return bool(result.scalar())


async def get_user_group(
        user_id: int,
        group_chat_id: int
) -> UsersGroups:
    """Получение информации о пользователе и группе."""
    current_session = await session_factory()
    async with current_session() as session:
        query_stmt = select(UsersGroups.id).where(
                and_(UsersGroups.user_id == user_id, UsersGroups.group_id == group_chat_id))
        result = await session.execute(query_stmt)
        return result.scalars().one()


async def get_all_users(group_id: int) -> Sequence[Users]:
    """Получение всех пользователей"""
    current_session = await session_factory()
    async with current_session() as session:
        query_stmt = (
            select(Users)
            .outerjoin(UsersGroups, UsersGroups.user_id == Users.user_id)
            .where(UsersGroups.group_id == group_id)
        )
        result = await session.execute(query_stmt)
        return result.scalars().all()


async def get_statistics(group_id: int) -> Sequence[Row[tuple[Any, Any]]]:
    """Получение статистики пользователей"""
    current_session = await session_factory()
    async with current_session() as session:
        query_stmt = (
            select(
                    Users.username,
                    (func.count(FoundErrors.user_group_id)).label("count_errors")
            )
            .outerjoin(UsersGroups, UsersGroups.user_id == Users.user_id)
            .outerjoin(FoundErrors, FoundErrors.user_group_id == UsersGroups.id)
            .where(UsersGroups.group_id == group_id)
            .group_by(Users.username)
            .order_by(func.count(FoundErrors.user_group_id).desc())
        )
        result = await session.execute(query_stmt)
        return result.all()


async def collect_errors(
        user_id: int,
        group_id: int,
        misspelled_word: str,
        correct_word: str,

) -> None:
    """
    Сбор статистики ошибок пользователя.
    :param user_id: Id пользователя
    :param misspelled_word: неправильное слово
    :param correct_word: корректное слово
    :param group_id: id группы, если ошибка в группе
    """
    user_group = await get_user_group(user_id, group_id)

    current_session = await session_factory()
    new_error = FoundErrors(
            user_group_id=user_group,
            misspelled_word=misspelled_word,
            correct_word=correct_word
    )
    async with current_session() as session:
        session.add(new_error)
        await session.commit()


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
