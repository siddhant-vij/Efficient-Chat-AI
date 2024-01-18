import openai
from typing import Optional, Tuple


class OpenAIApiClient:
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key
        self.client = openai.OpenAI(api_key=api_key)

    def send_chat_message(self, messages: list) -> Optional[openai.ChatCompletion]:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=messages
            )
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def extract_response(self, api_response: openai.ChatCompletion) -> Tuple[Optional[str], int, int, int]:
        if api_response:
            assistant_message = api_response.choices[0].message.content
            prompt_tokens = api_response.usage.prompt_tokens
            response_tokens = api_response.usage.completion_tokens
            total_tokens = api_response.usage.total_tokens
            return assistant_message, prompt_tokens, response_tokens, total_tokens
        return None, 0, 0, 0
