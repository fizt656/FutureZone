# FutureZone: Prototype TPZ Advisor Discord Bot

**IMPORTANT: This is a functional prototype to demonstrate utility. It is not a finished product... YET.**

This project prototypes a Discord bot that supports TPZ (The Possible Zone) Advisors, helping students navigate their entrepreneurial journey. The bot supports multiple characters, text-to-speech functionality, and integration with different language models.

Repository URL: https://github.com/fizt656/FutureZone.git

## Prototype Status

This bot is currently in a prototype stage. It serves as a demonstration of the concept and functionality, but is not yet optimized for production use. Features may be incomplete or subject to change as the project evolves.

## Features

- Conversation management with TPZ Advisors
- Text-to-speech functionality using ElevenLabs (prototype integration)
- Support for multiple AI models (Claude, OpenRouter)
- Character selection when launching the bot
- Basic command system for interaction within Discord

## Main Components

- `main.py`: Entry point of the application, contains Discord event handlers and commands
- `api_manager.py`: Manages API calls to different AI models
- `conversation_manager.py`: Manages conversation state and history
- `tts_manager.py`: Manages text-to-speech functionality
- `characters.py`: Defines character information and system prompts
- `config.py`: Configuration file (not included in repository for security reasons)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/fizt656/FutureZone.git
   cd FutureZone
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the configuration file:
   - Copy `config_template.py` to `config.py`
   - Open `config.py` and replace the placeholder values with your actual API keys and tokens:
     - Anthropic API key
     - OpenRouter API key
     - ElevenLabs API key
     - Discord bot token
     - Discord user ID

5. Run the bot:
   ```
   python main.py [character_name]
   ```
   If no character name is provided, the bot will default to "Eli".

## Usage

- `!delete`: Delete the last message in the conversation
- `!clear`: Clear the conversation history
- `!tts`: Toggle text-to-speech mode
- `!say [message]`: Generate TTS for the specified message
- `!quit`: Shut down the bot

Note: As this is a prototype, command functionality may be limited or subject to change.

## Contributing

This project is in its early stages and is primarily a proof-of-concept. While we welcome feedback and suggestions, please note that major contributions or changes may be deferred until the project moves beyond the prototype phase.

If you'd like to contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive messages
4. Push your changes to your fork
5. Create a pull request to the main repository

Please ensure your code follows the project's coding style and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is a prototype and is not intended for production use in its current state. It may contain bugs, incomplete features, or security vulnerabilities.