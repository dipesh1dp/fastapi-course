# from pydantic import BaseSettings (deprecated)
# Pydantic v2 uses pydantic_settings for settings management.
# BaseSettings is used to create settings classes that can read from environment variables.
# Field is used to provide additional metadata and validation for each setting. 
from pydantic_settings import BaseSettings
from pydantic import Field 

class Settings(BaseSettings):
    # Pydantic v2 does NOT automatically map uppercase env names to lowercase field names unlike v1.
    # So we use Field with alias to specify the exact env variable name.
    # ... (Ellipsis) is used to mark a field as required.
    # Fields without a default value are automatically required so ... is optional here.
    database_port: str = Field(..., alias="DATABASE_PORT")
    database_hostname: str = Field(alias="DATABASE_HOSTNAME") 
    database_password: str = Field(alias="DATABASE_PASSWORD")
    database_name: str = Field(alias="DATABASE_NAME")
    database_username: str = Field(alias="DATABASE_USERNAME")
    
    secret_key: str = Field(alias="SECRET_KEY")
    algorithm: str = Field(alias="ALGORITHM")
    access_token_expire_minutes: int = Field(alias="ACCESS_TOKEN_EXPIRE_MINUTES")

    # Specify the .env file to load environment variables from.
    class Config:
        env_file = ".env"

settings = Settings() 
