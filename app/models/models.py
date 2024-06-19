from sqlalchemy import ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, Mapped

from app.models.domains import created_at, modified_at, intpk, intpk_fk, str128, str256


class BaseModel(DeclarativeBase):
    """
    Базовый класс для всех моделей
    DeclarativeBase - базовый класс для всех моделей, используется для создания базы данных
    является аналогом MetaData в sqlalchemy, используемого для императивного создания таблиц
    """

    # Поле даты, например дата создания
    created_at: Mapped[created_at]
    # Поле даты, например дата изменения
    modified_at: Mapped[modified_at]


class Users(BaseModel):
    """Объект модели Users"""

    __tablename__ = "users"
    # Mapped[int] - это аналог Column, в котором так же можно указать тип
    # mapped_column - это декларативный способ создания столбца
    user_id: Mapped[intpk_fk]
    username: Mapped[str128]
    first_name: Mapped[str128]
    last_name: Mapped[str128]


class Restaurant(BaseModel):
    __tablename__ = "restorans"
    id: Mapped[intpk]
    name: Mapped[str128]


class Dish(BaseModel):
    __tablename__ = "dish"
    id: Mapped[intpk]
    name: Mapped[str128]
    price: Mapped[float]


class DishOrders(BaseModel):
    __tablename__ = "dish_orders"
    id: Mapped[intpk]
    user_id: Column[Mapped[intpk_fk], ForeignKey("users.user_id")]


class Events(BaseModel):
    __tablename__ = "events"
    id: Mapped[intpk]
    restaurant_id: Mapped[intpk_fk]
    user_id: Mapped[intpk_fk]
    order_id: Mapped[intpk_fk]
    link_to_pay: Mapped[str256]



