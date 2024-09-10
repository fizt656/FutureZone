![FutureZone Banner](banner.png)

# FutureZone: Prototype TPZ Advisor Discord Bot

**IMPORTANT: This is a functional prototype to demonstrate utility. It is not a finished product... YET.**

This project prototypes a Discord bot that supports TPZ (The Possible Zone) Advisors, helping students navigate their entrepreneurial journey. The bot provides engaging, friction-free reflection opportunities and prompts to students, while also generating insight packages for TPZ educators and other stakeholders.

## Prototype Status

This bot is currently in a prototype stage. It serves as a demonstration of the concept and functionality, but is not yet optimized for production use. Features may be incomplete or subject to change as the project evolves.

## Purpose and Features

- Facilitate ongoing reflection and guidance for students throughout their TPZ journey
- Generate insight packages for TPZ educators, R&E, Student Support, and Communications (prototype stage)
- Conversation management with TPZ Advisors
- Text-to-speech functionality using ElevenLabs (now enabled by default)
- Support for multiple AI models (Claude, OpenRouter)
- Character selection when launching the bot, with character-specific voice settings
- Basic command system for interaction within Discord

## Main Components

- `main.py`: Entry point of the application, contains Discord event handlers and commands
- `api_manager.py`: Manages API calls to different AI models
- `conversation_manager.py`: Manages conversation state and history
- `tts_manager.py`: Manages text-to-speech functionality with character-specific settings
- `characters.py`: Defines character information, system prompts, and voice settings
- `config.py`: Configuration file (not included in repository for security reasons)

## Installation

There are two ways to install and configure FutureZone: one-click installation and manual installation.

### One-Click Installation

The one-click installation method provides a quick and easy way to set up FutureZone. However, it may not give you as much insight into the setup process as the manual method (in case you want to build later, especially in different environments).

1. Download the appropriate installer for your operating system:
   - For Windows: `install.bat`
   - For Mac/Linux: `install.sh`

2. Run the installer:
   - On Windows: Double-click the `install.bat` file
   - On Mac/Linux: Open a terminal, navigate to the directory containing `install.sh`, and run:
     ```
     chmod +x install.sh
     ./install.sh
     ```

3. Follow the prompts to enter your API keys and other configuration details.

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

The FutureZone bot is designed to engage with students in an informal, friendly manner. It uses emojis and casual language to create a comfortable environment for students to reflect on their entrepreneurial journey at The Possible Zone (TPZ).

### How It Works

1. When the bot is started, it automatically initiates the conversation by sending a greeting message to the student.
2. The bot introduces itself as the selected character (default is Elijah McCoy/Eli) and starts with a general check-in, asking how things are going in the student's life before transitioning to their progress at TPZ.
3. Students can engage in ongoing conversations with the bot, asking questions or reflecting on their work at TPZ.
4. The bot provides guidance and prompts related to the different phases of the TPZ program:
   - DISCOVER: Introduction to TPZ facilities and initial projects
   - EXPLORE: Deeper exploration of chosen zones and iteration on methods and tools
   - CREATE: Development of a business idea based on experiences in DISCOVER and EXPLORE
5. The bot can also discuss other TPZ opportunities like STEAM Deep Dives, Open Studio, and College and Career Pathways Bootcamps.
It will be up to US to work together and train this with some materials/prompt as a team, looking forward to your partnership on that!

### Commands

- `!delete`: Delete the last message in the conversation
- `!clear`: Clear the conversation history
- `!tts`: Toggle text-to-speech mode on or off (TTS is enabled by default)
- `!say [text]`: Generate TTS for the specified text
- `!quit`: Shut down the bot

### Text-to-Speech (TTS) Feature

The TTS feature is now enabled by default, providing a more immersive and accessible experience. It uses character-specific voice settings defined in `characters.py`. The bot's responses are automatically converted to speech using the ElevenLabs API.

## Insight Packages (NOT live yet, in development)

While interacting with students, the bot generates insight packages for various stakeholders:

1. TPZ Educators: Receive summaries of student interactions, progress, and potential areas for support.
2. R&E (Research and Evaluation): Gain data on student engagement, common themes, and program effectiveness.
3. Student Support: Receive alerts on students who may need additional assistance or resources.
4. Communications: Gather stories and highlights that can be used for program promotion and reporting (future feature).

Note: In this prototype stage, the insight package generation is simulated and not fully implemented.

## Future Plans

As this project evolves beyond the prototype stage, we aim to implement:

1. Advanced context-based flagging system to alert relevant stakeholders (e.g., student support, educators) based on conversational cues, not just keywords.
2. Integration with TPZ's existing systems for seamless data flow and insights sharing.
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