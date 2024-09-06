from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship

import click
from flask import current_app, g

from typing import List, Optional


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    sex: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Sex(Base):
    __tablename__ = "sex"

    id: Mapped[int] = mapped_column(primary_key=True)
    sex: Mapped[str] = mapped_column(String(30))


engine = create_engine('sqlite:///database.db', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))


@click.command('init-db')
def init_db_command():
    # """Clear the existing data and create new tables."""
    # init_db()
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        male = Sex(id=1, sex='Male')
        female = Sex(id=2, sex='Female')
        session.add(male, female)
        session.commit()
        click.echo('Initialized the database.')


def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
