import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    database_url: str = os.getenv("DB_URL")


settings = Settings()