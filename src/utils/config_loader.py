import os
from dotenv import load_dotenv


class ConfigLoader:
    def __init__(self) -> None:
        load_dotenv()
        self.api_key: str = os.getenv('OPENAI_API_KEY', '')

    def get_api_key(self) -> str:
        return self.api_key
