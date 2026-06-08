import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    database_url: str = os.getenv("DB_URL")
    jwt_secret: str = os.getenv("JWT_SECRET", "changeme")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24


settings = Settings()