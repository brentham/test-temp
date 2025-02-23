from src.config.database import settings, engine
from sqlmodel import Session

# Dependency for SQL DB
def get_db():
    if settings.DB_TYPE in ["postgres", "mysql", "mssql"]:
        with Session(engine) as session:
            yield session