import openai
import logging
from typing import Optional, Tuple


class OpenAIApiClient:
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key
        openai.api_key = self.api_key
        logging.basicConfig(level=logging.INFO)

    def send_chat_message(self, messages: list) -> Optional[openai.ChatCompletion]:
        try:
            response = openai.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=messages
            )
            return response
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            return None

    def extract_response(self, api_response: openai.ChatCompletion) -> Tuple[Optional[str], int, int, int]:
        if api_response:
            assistant_message = api_response.choices[0].message.content
            prompt_tokens = api_response.usage.prompt_tokens
            response_tokens = api_response.usage.completion_tokens
            total_tokens = api_response.usage.total_tokens
            return assistant_message, prompt_tokens, response_tokens, total_tokens
        return None, 0, 0, 0
