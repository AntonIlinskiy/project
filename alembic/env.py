import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✅ Добавляем путь до корня проекта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ⬇️ Импорты из твоего приложения
from app.database import SQLALCHEMY_DATABASE_URL, Base  # noqa

# Настройки логирования из alembic.ini
fileConfig(context.config.config_file_name)

# Конфигурация Alembic
config = context.config
config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)

# Целевая мета-информация
target_metadata = Base.metadata


def run_migrations_offline():
    """Миграции в оффлайн-режиме (без подключения к БД)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Миграции в онлайн-режиме (с подключением к БД)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Определяем режим и запускаем нужную функцию
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
