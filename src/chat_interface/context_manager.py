class ContextManager:
    """
    Manages the conversation context.
    """

    def __init__(self):
        """
        Initializes the context manager.
        """
        self.context = ""

    def update_context(self, user_message, assistant_message):
        """
        Updates the context with the latest exchange.
        :param user_message: The latest message from the user.
        :param assistant_message: The latest response from the assistant.
        """
        pass

    def get_context(self):
        """
        Retrieves the current conversation context.
        :return: The current context.
        """
        pass
