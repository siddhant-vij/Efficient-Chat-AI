from src.utils.config_loader import ConfigLoader
from src.openai_api.api_client import OpenAIApiClient
from src.chat_interface.context_manager import ContextManager
from src.chat_interface.token_counter import TokenCounter
from src.chat_interface.state_manager import StateManager
from src.chat_interface.chat_manager import ChatManager
from src.utils.token_analytics import calculate_token_cost
import datetime


def display_conversation_options(state_manager: StateManager):
    past_states = state_manager.load_state()
    if not past_states:
        print("No past conversations found. Starting a new one.")
        return None

    print("Past Conversations:")
    for idx, state in enumerate(past_states):
        print(
            f"{idx + 1}: (Timestamp: {state['timestamp']}) {state['summary']}")

    choice = input(
        "Choose a conversation to resume (or 'new' for a new conversation): ")
    if choice.lower() == 'new':
        return None
    elif choice.isdigit() and 1 <= int(choice) <= len(past_states):
        return past_states[int(choice) - 1]['details']
    else:
        print("Invalid choice. Starting a new conversation.")
        return None


def get_one_line_summary(text: str, max_words: int = 15) -> str:
    return ' '.join(text.split()[:max_words])


def main():
    api_key = ConfigLoader().get_api_key()

    api_client = OpenAIApiClient(api_key)
    context_manager = ContextManager()
    token_counter = TokenCounter()
    state_manager = StateManager()
    chat_manager = ChatManager(
        api_client, context_manager, token_counter, state_manager)

    conversation_id = state_manager.generate_conversation_id()
    previous_context = display_conversation_options(state_manager)

    if previous_context:
        context_manager.update_context(previous_context, "")
    else:
        conversation_id = state_manager.generate_conversation_id()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            one_line_summary = get_one_line_summary(
                ' '.join(context_manager.get_context()))
            state_manager.save_state(conversation_id, {
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'summary': one_line_summary,
                'details': context_manager.get_context()
            })
            print("Exiting chat...")
            break

        response, prompt_tokens, response_tokens, total_tokens = chat_manager.process_user_input(
            user_input)
        print(f"AI: {response}")

        print(
            f"Token usage - Prompt: {prompt_tokens}, Response: {response_tokens}, Total: {total_tokens}")
        print(
            f"Estimated cost: ${calculate_token_cost(prompt_tokens, response_tokens):.4f}")

        chat_manager.update_conversation(user_input, response)

        # Handle token limit reached
        if token_counter.check_token_limit():
            print("Token limit reached.")
            choice = input(
                "Choose an option - 1: Reduce context, 2: Download summary and reset: ")
            if choice == '1':
                context_manager.reduce_context()
            elif choice == '2':
                summary_file_name = get_one_line_summary(
                    ' '.join(context_manager.get_context())).replace(' ', '_')
                context_manager.save_conversation_as_docx(
                    get_one_line_summary(response), context_manager.get_context(), summary_file_name)
                print("Summary downloaded. Resetting conversation.")
                context_manager.reset_context()


if __name__ == "__main__":
    main()
