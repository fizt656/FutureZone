![FutureZone Banner](banner.png)

# FutureZone: Prototype Advisor Discord Bot

**IMPORTANT: This is a functional prototype to demonstrate utility. It is not a finished product... YET.**

This project prototypes a Discord bot that supports teachers, mentors, career advisors, and life coaches. The bot provides engaging, friction-free reflection opportunities and prompts to students, while also generating insight packages for mentors and other stakeholders.

## About the Demo Version

In this demo, the bot is configured as an advisor for the fictional Hogwarts School of Witchcraft and Wizardry. The default character, Elijah "Eli" McCoy, guides students through their magical education journey. As Albus Dumbledore once said, "It is our choices that show what we truly are, far more than our abilities." This advisor bot aims to help students make those important choices.

**Note to Users:** While the demo uses a fictional setting, you can easily customize the bot for your specific educational context. The `characters.py` file contains the system prompt and character settings, which you can modify to suit your needs. Feel free to replace Hogwarts with your own institution and adjust the educational journey to match your curriculum!

## Prototype Status

This bot is currently in a prototype stage. It serves as a demonstration of the concept and functionality, but is not yet optimized for production use. Features may be incomplete or subject to change as the project evolves.

## Purpose and Features

- Facilitate ongoing reflection and guidance for students throughout their journey
- Generate insight packages for various stakeholders (prototype stage)
- Conversation management with mentors
- Text-to-speech functionality using ElevenLabs (now enabled by default)
- Support for multiple AI models (Claude, OpenRouter)
- Character selection when launching the bot, with character-specific voice settings (allowing user to customize to their needs and environment)
- Basic command system for interaction within Discord

## Main Components

- `main.py`: Entry point of the application, contains Discord event handlers and commands
- `api_manager.py`: Manages API calls to different AI models
- `conversation_manager.py`: Manages conversation state and history
- `tts_manager.py`: Manages text-to-speech functionality with character-specific settings
- `characters.py`: Defines character information, system prompts, and voice settings
- `config.py`: Configuration file (generated for you during one-click installation, otherwise, use the template to set yours up)

## Installation

There are two ways to install and configure FutureZone: one-click installation and manual installation.

### One-Click Installation

The one-click installation method provides a quick and easy way to set up FutureZone. However, it may not give you as much insight into the setup process as the manual method (in case you want to build later, especially in different environments).

1. Clone the repository:
   ```
   git clone https://github.com/fizt656/FutureZone.git
   cd FutureZone
   ```

2. Run the appropriate installer for your operating system:
   - On Windows: Double-click the `install.bat` file or run it from the command prompt
   - On Mac/Linux: Open a terminal and run:
     ```
     chmod +x install.sh
     ./install.sh
     ```

3. Follow the prompts to enter your API keys and other configuration details.

4. After the installation is complete, you can run the bot using:
   ```
   python main.py [character_name]
   ```
   If no character name is provided, the bot will default to "Eli".

### Manual Installation

With manual installation, you'll have more control over the setup process and potentially learn more about the project structure. Here are the steps:

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
     - OpenRouter API key and HTTP Referer
     - ElevenLabs API key and Voice ID
     - Discord bot token and user ID

5. Run the bot:
   ```
   python main.py [character_name]
   ```
   If no character name is provided, the bot will default to "Eli".

## Usage

The FutureZone bot is designed to engage with students in an informal, friendly manner. It uses emojis and casual language to create a comfortable environment for students to reflect on their journey.

### How It Works

1. When the bot is started, it automatically initiates the conversation by sending a greeting message to the student.
2. The bot introduces itself as the selected character (default is Elijah McCoy/Eli) and starts with a general check-in, asking how things are going in the student's life before transitioning to their progress.
3. Students can engage in ongoing conversations with the bot, asking questions or reflecting on their work.
4. The bot provides guidance and prompts related to different phases of the journey.

### Commands

- `!delete`: Delete the last message in the conversation
- `!clear`: Clear the conversation history
- `!tts`: Toggle text-to-speech mode on or off (TTS is enabled by default)
- `!say [text]`: Generate TTS for the specified text
- `!quit`: Shut down the bot

### Text-to-Speech (TTS) Feature

The TTS feature is enabled by default, providing a more immersive and accessible experience. It uses character-specific voice settings defined in `characters.py`. The bot's responses are automatically converted to speech using the ElevenLabs API.

## Insight Packages (NOT live yet, in development)

While interacting with students, the bot will [eventually be able to -- growth mindset, right?] generate insight packages for various stakeholders:

1. Mentors: Receive summaries of student interactions, progress, and potential areas for support.
2. Researchers: Gain data on student engagement, common themes, and program effectiveness.
3. Counselors: Receive alerts on students who may need additional assistance or resources.
4. Communication Officers: Gather stories and highlights that can be used for program promotion and reporting (future feature).

Note: In this prototype stage, the insight package generation is NOT implemented... YET.

## Future Plans

As this project evolves beyond the prototype stage, we aim to implement:

1. Advanced context-based flagging system to alert relevant stakeholders based on conversational cues, not just keywords.
2. Integration with existing educational systems for seamless data flow and insights sharing.
3. Expanded character roster to provide diverse perspectives and expertise.
4. Enhanced natural language processing for more nuanced understanding of student needs and progress.
5. Further improvements to multimodal interaction capabilities, building on the current TTS implementation.

## Contributing

This project is in its early stages and is primarily a proof-of-concept. While we welcome feedback and suggestions, please note that major contributions or changes may be deferred until the project moves beyond the prototype phase.

If you'd like to contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive messages
4. Push your changes to your fork
5. Create a pull request to the main repository

Please ensure your code follows the project's coding style and includes appropriate documentation.

## Disclaimer

This bot is a prototype and is not intended for production use in its current state. It may contain bugs, incomplete features, or security vulnerabilities.

## License

This project is licensed under a dual license. Please see the LICENSE file for details.