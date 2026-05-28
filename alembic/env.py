import sys
import os
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv

# 1. Setup path and load config
sys.path.append(os.getcwd())
load_dotenv()

# 2. Import Base and set metadata
from app.core.database import Base

#my tables
#from app.models.entity import Entity
#from app.models.prompt import Prompt
# replaced the above 2 lines with this import
import app.models  # This triggers the code in app/models/__init__.py

target_metadata = Base.metadata

# 3. Alembic config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 4. Migration logic
def run_migrations_online() -> None:
    # Use your DATABASE_URL from your .env
    connectable = create_engine(os.getenv("DATABASE_URL"))

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    # Keep offline support if needed, otherwise this is fine
    context.configure(url=os.getenv("DATABASE_URL"), target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations_online()