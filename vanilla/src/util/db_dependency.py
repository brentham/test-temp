from src.config.database import settings, engine
from sqlmodel import Session

# Dependency for SQL DB
def get_db():
    if settings.DATABASE_CLIENT in ["postgres", "mysql", "mssql", "sqlite"]:
        with Session(engine) as session:
            yield session