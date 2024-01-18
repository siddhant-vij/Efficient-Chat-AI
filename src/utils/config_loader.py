import os
from dotenv import load_dotenv


class ConfigLoader:
    def __init__(self) -> None:
        load_dotenv()
        self.api_key: str = os.getenv('OPENAI_API_KEY', '')
        self.summary_ratio: float = os.getenv('SUMMARY_RATIO', '0.3')
        self.token_limit: int = os.getenv('TOKEN_LIMIT', '8000')

    def get_api_key(self) -> str:
        return self.api_key
    
    def get_summary_ratio(self) -> float:
        return self.summary_ratio
    
    def get_token_limit(self) -> int:
        return self.token_limit
