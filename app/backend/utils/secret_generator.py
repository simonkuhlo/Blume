import random
import settings

def generate_secret(length: int = settings.entries.default_secret_length, allowed_chars: str = settings.entries.allowed_chars) -> str:
    secret: str = ""
    for index in range(length):
        secret += random.SystemRandom().choice(allowed_chars)
    return secret