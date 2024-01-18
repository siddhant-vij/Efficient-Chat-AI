from typing import Optional, Tuple
from chat_interface.context_manager import ContextManager
from chat_interface.state_manager import StateManager
from chat_interface.token_counter import TokenCounter
from openai_api.api_client import OpenAIApiClient


class ChatManager:
    def __init__(self, api_client: OpenAIApiClient, context_manager: ContextManager, token_counter: TokenCounter, state_manager: StateManager) -> None:
        self.api_client = api_client
        self.context_manager = context_manager
        self.token_counter = token_counter
        self.state_manager = state_manager

    def process_user_input(self, input_text: str) -> Optional[Tuple[str, int, int, int]]:
        context = self.context_manager.get_context_api()
        formatted_input = {"role": "user", "content": input_text}
        response = self.api_client.send_chat_message(
            context + [formatted_input])

        if response:
            assistant_response, prompt_tokens, response_tokens, total_tokens = self.api_client.extract_response(
                response)
            self.update_conversation(input_text, assistant_response)
            self.token_counter.update_token_count(
                prompt_tokens + response_tokens)
            return assistant_response, prompt_tokens, response_tokens, total_tokens
        return None

    def update_conversation(self, user_input: str, assistant_response: str) -> None:
        self.context_manager.update_context(user_input, assistant_response)
