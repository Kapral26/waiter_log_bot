
def error_msg(error_text: str | None = None) -> dict[str: str]:
    """
    Подготовленные параметры для отправки текста сообщения об ошибке.
    :param error_text: Текст ошибки.
    :return:
    """
    error = {
        "text": "Случилось что-то не предсказуемое" if not error_text else error_text
    }

    return error
