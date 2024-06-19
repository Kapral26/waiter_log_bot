"""Основной модуль для работы Telegram Bot."""

import asyncio

from aiogram import Bot, Dispatcher, types, html, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.formatting import as_list, as_marked_section, Bold, Text
from config.config_reader import Settings
from utils.basic_msg import error_msg
from utils.db.core import insert_user, get_all_users, check_registry_user, collect_errors, get_statistics
from utils.log import logger
from utils.ya_spell import use_yandexspeller

settings = Settings()

# Создать глобального бота
bot = Bot(
        token=settings.bot_token.get_secret_value()
)
dp = Dispatcher()


@dp.message(Command(commands=["help"]))
async def send_menu(message: types.Message) -> None:
    """Отправить список команд бота"""
    msg = as_list(
            Bold("Список команд:"),
            "/start - Запустить бота",
            "/registry - Регистрация пользователя",
            "/help - Помощь, собственно увидеть это сообщение",
            "/users - Показать список всех пользователей",
            "/statistics - Показать статистику"
    )
    await message.reply(
            **msg.as_kwargs(),
            reply=False,
    )


@dp.message(Command("start"))
async def send_welcome(message: types.Message) -> None:
    """Поприветствовать"""
    msg = Text(
            "Привет ",
            Bold(f"{message.from_user.first_name}!\n"),
            "Я - бот, который корректирует написание твоего текста!"
    )
    await message.reply(**msg.as_kwargs())

    if message.chat.type == "private":
        await registry_user(message)
    # Показать список команд
    await send_menu(message=message)


@dp.message(Command("registry"))
async def registry_user(message: types.Message) -> None:
    """Регистрация пользователя."""
    user_is_registry = await check_registry_user(
            user_id=message.from_user.id,
            group_chat_id=message.chat.id
    )

    if user_is_registry:
        await message.reply(
                "Ты уже зарегистрирован!",
                reply=False
        )
        return

    await insert_user(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            message.chat
    )

    await message.reply(
            f"""
            Пользователь: {html.bold(message.from_user.first_name)} Зарегистрирован
            """.strip(),
            parse_mode=ParseMode.HTML

    )


@dp.message(Command("users"))
async def users(message: types.Message) -> None:
    """Показать список пользователей"""
    all_users = await get_all_users(message.chat.id)

    formatted_users = [
        Text(
                Bold("\nusername: "), f"{user.username}\n",
                Bold("first_name: "), f"{user.first_name}\n",
                Bold("last_name: "), f"{user.last_name}\n",
                "-------\n"
        ) for user in all_users
    ]

    msg = as_list(
            as_marked_section(
                    Bold("Список пользователей:\n"),
                    *formatted_users,
                    marker="👤",
            )
    )

    await message.reply(**msg.as_kwargs())


@dp.message(Command("statistics"))
async def statistics(message: types.Message) -> None:
    """Показать список пользователей"""
    user_statistics = await get_statistics(message.chat.id)

    users_errors = [
        Text(
                Bold(f"{user[0]} : "),
                f"{user[1]} ошибки(ок)"
        ) for user in user_statistics
    ]
    msg = as_list(
            as_marked_section(
                    Bold("Статистика пользователей:\n"),
                    *users_errors,
                    marker="▪️",
            )
    )

    await message.reply(
            **msg.as_kwargs(),
    )


@dp.message(F.text)
async def cmd_spell(message: types.Message) -> None:
    """Проверяет правописание текста и заменяет все проблемные слова на корректные."""
    correct_text = message.text

    user_registry = await check_registry_user(
            user_id=message.from_user.id,
            group_chat_id=message.chat.id,
    )

    if not user_registry:
        # Собираем статистику только если пользователь зарегистрирован
        return

    try:
        result = await use_yandexspeller(correct_text)
    except Exception as error:
        logger.exception(error)
        await message.reply(**error_msg())
        raise

    for bad_w, corr_w in result:
        await collect_errors(
                message.from_user.id,
                message.chat.id,
                bad_w,
                corr_w
        )

        if message.chat.type == "private":
            correct_text = correct_text.replace(
                    bad_w,
                    corr_w
            )

    if message.chat.type == "private":
        await message.answer(
                text=correct_text,
                parse_mode=ParseMode.HTML
        )


async def main() -> None:
    """Основной метод запуска бота."""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
