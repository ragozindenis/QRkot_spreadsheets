from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд'
    database_url: str = 'sqlite+aiosqlite:///./QRkot.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    email: Optional[str] = None  # email google
    # api key google:
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    # Constants:
    JWT_LIFETIME: int = 3600
    MIN_PASSWORD_LENGTH: int = 3
    MAX_LENGTH = 100
    MIN_LENGTH = 1
    DEFAULT_VALUE_FULL_AMOUNT = 0
    DEFAULT_VALUE_INVESTED_AMOUNT = 0
    DEFALUT_VALUE_FULLY_INVESTED = 0
    FORMAT = "%Y/%m/%d %H:%M:%S"
    SHEET_ID = 0
    ROW_COUNT = 100
    COLUMN_COUNT = 11
    RANGE_UPDATE = 'A1:E30'

    class Config:
        env_file = '.env'


settings = Settings()
