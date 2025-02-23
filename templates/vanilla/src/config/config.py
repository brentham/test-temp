from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from urllib.parse import quote
import os

class Settings(BaseSettings):
    APP_NAME: str | None = None
    VERSION: str | None = None
    API_V1_STR: str = "/api/v1"
    
# Database Vars
    DB_URL: str | None = None
    DB_USERNAME: str | None = None
    DB_PASSWORD: str | None = None
    DB_URL: str | None = None
    DB_URL2: str | None = None
    DB_NAME: str | None = None
    DB_TYPE: str | None = None
    DATABASE_URL: str | None = None
    DB_DRIVER: str | None = None
    DB_PORT: str | None = None

# Azure SSO Vars
    # BACKEND_CORS_ORIGINS: list[str | None = None | AnyHttpUrl] = ['http://localhost:8000']
    TENANT_ID: str | None = None
    CLIENT_ID: str | None = None
    CLIENT_SECRET: str | None = None
    REDIRECT_URI: str | None = None
    AUTHORITY: str | None = None
    SCOPE: str | None = None

# Secret Key
    SECRET_KEY: str | None = None
    ALGORITHM: str = "HS256"
   
# Debug 
    # DEBUG: str | None = None
    
    
    @property
    def db_config(self) -> dict:
        """Database configuration dictionary."""
        db_password = quote(self.DB_PASSWORD or "")  # URL-encode password safely

        return {
            "postgres": f"postgresql://{self.DB_USERNAME}:{db_password}@{self.DB_URL}/{self.DB_NAME}",
            "mysql": f"mysql+pymysql://{self.DB_USERNAME}:{db_password}@{self.DB_URL}/{self.DB_NAME}",
            "mssql": f"mssql+pyodbc://{self.DB_USERNAME}:{db_password}@{self.DB_URL}/{self.DB_NAME}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes",
            "mongo": f"mongodb://{self.DB_USERNAME}:{db_password}@{self.DB_URL}/{self.DB_NAME}",
            "sqlite": f"sqlite:///{self.DB_NAME}.db"  # SQLite (if needed)
            # "sqlite": f"sqlite:///{os.path.abspath(self.DB_NAME)}.db"
        }

    @property
    def sqlalchemy_url(self) -> str:
        """Retrieve the SQLAlchemy database URL based on DB_TYPE."""
        if self.DB_TYPE in self.db_config:
            return self.db_config[self.DB_TYPE]
        else:
            raise ValueError(f"Unsupported database type: {self.DB_TYPE}")

    class Config:
        env_file = ".env"

settings = Settings()