"""Домены полей БД."""

from datetime import datetime
from typing import Annotated

from sqlalchemy import BigInteger, text, String
from sqlalchemy.orm import mapped_column

# Annotated - позволяет создать собственную аннотацию
# В дальнейшем их можно будет указывать в качестве типа при маппинге поля.
# Так же я могу сравнить это с доменами в Firebird.
intpk = Annotated[int, mapped_column(primary_key=True)]
intpk_fk = Annotated[int, mapped_column(autoincrement=False)]
bigint = Annotated[int, mapped_column(BigInteger, autoincrement=False, primary_key=True, unique=True)]

created_at = Annotated[
    datetime,
    mapped_column(
            default=datetime.now()  # Значение по умолчанию, данные берутся из python
    ),
]

modified_at = Annotated[
    datetime,
    mapped_column(
            server_default=text("CURRENT_TIMESTAMP"),
            # Значение по серверу, соответственно данные будут взяты с сервера
            onupdate=datetime.now,  # Значение по обновлению, но лучше задавать через триггер в БД.
    ),
]

str128 = Annotated[str, mapped_column(String(128), nullable=True, default="")]
str256 = Annotated[str, mapped_column(String(256), nullable=True, default="")]
