from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file='/Users/tianshani/Documents/Code/Python/trello-app/.env',
        extra='ignore'
    )

Config = Settings()