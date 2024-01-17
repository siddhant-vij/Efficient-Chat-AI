# Efficient Chat AI

A terminal-based chat application that leverages OpenAI's GPT-4 model to facilitate long-form conversations. It is designed with a focus on efficient token usage and robust context retention, ensuring cost-effective interactions without compromising the continuity and coherence of conversations.

## Table of Contents
1. [Features](#features)
1. [Installation](#installation)
1. [Contributions](#contributions)
1. [Future Improvements](#future-improvements)
1. [License](#license)

## Features
- **Dynamic Context Management**: Automatically manages conversation context to fit within token limits while retaining essential information.
- **Token-Efficient Communication**: Monitors and controls token usage to minimize API costs.
- **Contextual Summarization**: Utilizes NLP techniques to summarize lengthy conversation histories into concise context.
- **User Intent Tracking**: Keeps track of the conversation's direction for relevant context inclusion.
- **Cost and Token Analytics**: Provides real-time token usage and cost estimates for transparency.
- **Persistent Conversation State**: Allows conversations to be saved and resumed, maintaining continuity over multiple sessions.

## Installation
- Clone the repository: `git clone https://github.com/siddhant-vij/Efficient-Chat-AI.git`
- Navigate to the project directory: `cd Efficient-Chat-AI`
- Create the conda environment: `conda create --name chat-ai python=3.10.13`
- Activate the environment: `conda activate chat-ai`
- Install dependencies: `pip install -r requirements.txt`
- Create a `.env` file in the project root directory based on the `.env.example` template.
- Install the package: `pip install .`
- Run the application: `chat-ai`

## Contributions
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. **Fork the Project**
1. **Create your Feature Branch**: 
    ```bash
    git checkout -b feature/AmazingFeature
    ```
1. **Commit your Changes**: 
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
1. **Push to the Branch**: 
    ```bash
    git push origin feature/AmazingFeature
    ```
1. **Open a Pull Request**

## Future Improvements
- **Interactive Chat UI**: Develop a more interactive and user-friendly graphical user interface (GUI) for the chat application. This could include features like conversation threading, real-time response updates, and support for multimedia content.
- **Multi-Language Support**: Expand the application to support multiple languages, allowing users from different linguistic backgrounds to interact with the AI in their native language.
- **Voice Recognition and Synthesis**: Integrate voice recognition for input and text-to-speech technologies for output. This would allow users to have spoken conversations with the AI, making the experience more accessible and engaging.
- **Advanced Context Management**: Implement more sophisticated algorithms for context management that can handle even longer conversations without losing coherence. This might include AI-driven summarization techniques and context prioritization based on user behavior.
- **User Personalization**: Introduce user profiles that allow for personalized experiences based on past interactions, preferences, and user-specific data.
- **Open Source Models**: Explore possibilities for replacing the OpenAI API with other Open Source Models & set it all up locally - could be packaged as an offline mode feature.

## License
Distributed under the MIT License. See [`LICENSE`](https://github.com/siddhant-vij/Efficient-Chat-AI/blob/main/LICENSE) for more information.