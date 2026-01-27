# config.py
from pathlib import Path
from pydantic import BaseModel, Field
import json

BASE_DIR = Path(__file__).resolve().parent

class NetworkSettings(BaseModel):
    host: str = Field(default="127.0.0.1")
    port: int = Field(default=8000, ge=1, le=65535)

class SystemSettings(BaseModel):
    pass

class UserSettings(BaseModel):
    max_entries: int = Field(default=1) # -1 = no limit

class Settings(BaseModel):
    network: NetworkSettings = NetworkSettings()
    system: SystemSettings = SystemSettings()
    user: UserSettings = UserSettings()

    @classmethod
    def from_json(cls, path: Path) -> "Settings":
        with path.open() as f:
            data = json.load(f)
        return cls(**data)

# load from JSON once at import time
settings = Settings.from_json(BASE_DIR / "settings.json")

if __name__ == "__main__":
    print(settings)
