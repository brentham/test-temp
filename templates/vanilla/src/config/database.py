from src.config.config import settings
from pymongo import MongoClient
from sqlmodel import SQLModel, create_engine

# Select database and initialize connections
if settings.DB_TYPE in ["postgres", "mysql", "mssql", "sqlite"]:
    engine = create_engine(settings.sqlalchemy_url)
    SQLModel.metadata.create_all(engine)
elif settings.DB_TYPE == "mongo":
    mongo_client = MongoClient(settings.sqlalchemy_url)
    mongo_db = mongo_client.get_database()
else:
    raise ValueError(f"Unsupported database type: {settings.DB_TYPE}")