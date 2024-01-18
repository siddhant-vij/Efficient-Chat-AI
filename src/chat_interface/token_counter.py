from src.utils.config_loader import ConfigLoader


class TokenCounter:
    def __init__(self) -> None:
        self.total_tokens: int = 0
        self.limit: int = int(ConfigLoader().get_token_limit())

    def update_token_count(self, token_count: int) -> None:
        self.total_tokens += token_count

    def check_token_limit(self) -> bool:
        return self.total_tokens >= self.limit
