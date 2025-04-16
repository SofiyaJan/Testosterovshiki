from logging.config import fileConfig
import sys
from os.path import abspath, dirname

from sqlalchemy import engine_from_config, pool
from alembic import context

# абсолютные импорты
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# импорт базы и моделей
from app.config import settings
from app.database import Base  # Убедись, что путь до database.py верный

from app.Users.models import User, Motivation
from app.Analyses.models import Analysis, Recommendation
from app.Diets.models import Diet, DietProduct
from app.Goals.models import Goal
from app.Products.models import Product

# конфиг из alembic.ini
config = context.config

# преобразуем asyncpg → psycopg2
#sync_url = str(make_url(DATABASE_URL).set(drivername="postgresql+psycopg2"))
# config.set_main_option("sqlalchemy.url", sync_url)
config.set_main_option("sqlalchemy.url", f"{settings.DATABASE_URL}?async_fallback=True")

# логгеры
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
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
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
