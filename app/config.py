from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()

# Debug: Print the database_url
print("Database URL:", settings.database_url)
