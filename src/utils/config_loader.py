import os
from dotenv import load_dotenv


class ConfigLoader:
    """
    Loads configuration settings from an .env file.
    """

    def __init__(self):
        """
        Initializes the config loader and loads the settings.
        """
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

    def get_api_key(self):
        """
        Retrieves the OpenAI API key.
        :return: The OpenAI API key.
        """
        return self.api_key
