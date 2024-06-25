"""Основной модуль для работы Telegram Bot."""

import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.formatting import as_list, Bold, Text

from config.config_reader import Settings

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
            "/help - Помощь, собственно увидеть это сообщение",
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

    # Показать список команд
    await send_menu(message=message)


@dp.message(Command("regular_button"))
async def regular_button(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,  # Уменьшить размер кнопок
            input_field_placeholder="Выберите способ подачи"  # Текст, который будет указан в поле ввода
    )
    await message.answer(
            "Как подавать котлеты?",
            reply_markup=keyboard
    )


@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply(
            "Отличный выбор!",
            reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply(
            "Так невкусно!",
            reply_markup=types.ReplyKeyboardRemove()
    )

# новый импорт
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )
    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )

    # Чтобы иметь возможность показать ID-кнопку,
    # У юзера должен быть False флаг has_private_forwards
    # user_id = 1234567890
    # chat_info = await bot.get_chat(user_id)
    # if not chat_info.has_private_forwards:
    #     builder.row(types.InlineKeyboardButton(
    #         text="Какой-то пользователь",
    #         url=f"tg://user?id={user_id}")
    #     )

    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )

async def main() -> None:
    """Основной метод запуска бота."""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
