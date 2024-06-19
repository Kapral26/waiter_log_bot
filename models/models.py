from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models.domains import created_at, modified_at, intpk, intpk_fk, str128, str256


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей
    DeclarativeBase - базовый класс для всех моделей, используется для создания базы данных
    является аналогом MetaData в sqlalchemy, используемого для императивного создания таблиц
    """

    # Поле даты, например дата создания
    created_at: Mapped[created_at]
    # Поле даты, например дата изменения
    modified_at: Mapped[modified_at]


class Users(Base):
    """Объект модели Users"""

    __tablename__ = "users"
    # Mapped[int] - это аналог Column, в котором так же можно указать тип
    # mapped_column - это декларативный способ создания столбца
    user_id: Mapped[intpk]
    username: Mapped[str128]
    first_name: Mapped[str128]
    last_name: Mapped[str128]


class Restaurant(Base):
    """Объект модели Restaurant"""

    __tablename__ = "restaurant"
    id: Mapped[intpk]
    name: Mapped[str128]


class Dish(Base):
    """Объект модели Dish"""

    __tablename__ = "dish"
    id: Mapped[intpk]
    name: Mapped[str128]
    price: Mapped[float]


class DishOrders(Base):
    """Объект модели DishOrders"""

    __tablename__ = "dish_orders"
    id: Mapped[intpk]
    user_id: Mapped[intpk_fk] = mapped_column(
            ForeignKey(
                    "users.user_id",
                    ondelete="CASCADE"
            )
    )
    dish_id: Mapped[intpk_fk] = mapped_column(
            ForeignKey(
                    "dish.id",
                    ondelete="CASCADE"
            )
    )


class Events(Base):
    """Объект модели Events"""

    __tablename__ = "events"
    id: Mapped[intpk]
    restaurant_id: Mapped[intpk_fk] = mapped_column(
            ForeignKey(
                    "restaurant.id",
                    ondelete="CASCADE"
            )
    )
    user_id: Mapped[intpk_fk] = mapped_column(
            ForeignKey(
                    "users.user_id",
                    ondelete="CASCADE"
            )
    )
    order_id: Mapped[intpk_fk] = mapped_column(
            ForeignKey(
                    "dish_orders.id",
                    ondelete="CASCADE"
            )
    )
    link_to_pay: Mapped[str256]
