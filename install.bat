@echo off

REM Create FutureZone directory
mkdir FutureZone
cd FutureZone

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.7 or higher and run this script again.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip and run this script again.
    exit /b 1
)

REM Clone the repository
git clone https://github.com/fizt656/FutureZone.git .

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Install requirements
pip install -r requirements.txt

REM Create config.py with user input
echo # config.py - Generated by install script > config.py
echo. >> config.py

echo from characters import characters >> config.py
echo. >> config.py

echo # OpenRouter API configuration >> config.py
set /p OPENROUTER_KEY="Enter your OpenRouter API key: "
echo OPENROUTER_KEY = '%OPENROUTER_KEY%' >> config.py
echo OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions' >> config.py
set /p HTTP_REFERER="Enter your HTTP Referer for OpenRouter: "
echo OPENROUTER_HEADERS = { >> config.py
echo     'Authorization': f'Bearer {OPENROUTER_KEY}', >> config.py
echo     'HTTP-Referer': '%HTTP_REFERER%', >> config.py
echo     'X-Title': 'TPZ-Advisor-Bot', >> config.py
echo     'Content-Type': 'application/json' >> config.py
echo } >> config.py
echo. >> config.py

echo CLAUDE_MODELS = { >> config.py
echo     "claude-3-opus-20240229": "3opus", >> config.py
echo     "claude-3-5-sonnet-20240620": "35sonnet" >> config.py
echo } >> config.py
echo. >> config.py

echo OPENROUTER_MODELS = { >> config.py
echo     "openai/gpt-4-turbo-preview": "gpt4t", >> config.py
echo     "anthropic/claude-3-opus-20240229": "c3opus", >> config.py
echo     "google/gemini-pro": "gemini", >> config.py
echo     "meta-llama/llama-2-70b-chat": "llama70b", >> config.py
echo     "mistralai/mistral-7b-instruct": "mistral7b", >> config.py
echo     "huggingfaceh4/zephyr-7b-beta": "zephyr7b" >> config.py
echo } >> config.py
echo OPENROUTER_MODEL = list(OPENROUTER_MODELS.keys())[0] >> config.py
echo OPENROUTER_TEMPERATURE = 0.7 >> config.py
echo OPENROUTER_MAX_TOKENS = 2048 >> config.py
echo. >> config.py

echo # Anthropic API configuration >> config.py
set /p ANTHROPIC_API_KEY="Enter your Anthropic API key: "
echo ANTHROPIC_API_KEY = '%ANTHROPIC_API_KEY%' >> config.py
echo ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages' >> config.py
echo ANTHROPIC_HEADERS = { >> config.py
echo     'X-API-Key': ANTHROPIC_API_KEY, >> config.py
echo     'Content-Type': 'application/json', >> config.py
echo     'anthropic-version': '2023-06-01' >> config.py
echo } >> config.py
echo ANTHROPIC_MODEL = 'claude-3-opus-20240229' >> config.py
echo ANTHROPIC_MAX_TOKENS = 1024 >> config.py
echo. >> config.py

echo # Set the default Claude model >> config.py
echo DEFAULT_CLAUDE_MODEL = "claude-3-opus-20240229" >> config.py
echo. >> config.py

echo # ElevenLabs API configuration >> config.py
set /p ELEVENLABS_API_KEY="Enter your ElevenLabs API key: "
echo ELEVENLABS_API_KEY = '%ELEVENLABS_API_KEY%' >> config.py
echo ELEVENLABS_API_URL = 'https://api.elevenlabs.io/v1/text-to-speech' >> config.py
set /p ELEVENLABS_VOICE_ID="Enter your ElevenLabs Voice ID: "
echo ELEVENLABS_DEFAULT_VOICE_ID = '%ELEVENLABS_VOICE_ID%' >> config.py
echo ELEVENLABS_HEADERS = { >> config.py
echo     'Content-Type': 'application/json', >> config.py
echo     'xi-api-key': ELEVENLABS_API_KEY, >> config.py
echo     'model_id': 'eleven_multilingual_v2', >> config.py
echo } >> config.py
echo ELEVENLABS_MODEL_ID = 'eleven_multilingual_v2' >> config.py
echo ELEVENLABS_VOICE_SETTINGS = { >> config.py
echo     'stability': 0.10, >> config.py
echo     'similarity_boost': 1, >> config.py
echo     'use_speaker_boost': True >> config.py
echo } >> config.py
echo. >> config.py

echo # Stable Diffusion API configuration >> config.py
echo STABLE_DIFFUSION_URL = 'http://127.0.0.1:7860/sdapi/v1/txt2img' >> config.py
echo. >> config.py

echo # Discord bot configuration >> config.py
set /p DISCORD_BOT_TOKEN="Enter your Discord bot token: "
echo DISCORD_BOT_TOKEN = '%DISCORD_BOT_TOKEN%' >> config.py
set /p DISCORD_USER_ID="Enter your Discord user ID: "
echo DISCORD_USER_ID = %DISCORD_USER_ID% >> config.py
echo. >> config.py

echo # Default LLM model >> config.py
echo DEFAULT_LLM = "anthropic"  # Can be "anthropic", "openrouter", or "lmstudio" >> config.py

echo Installation complete! A new config.py file has been created with your input.
echo The project has been set up in the 'FutureZone' directory.
echo To run the bot:
echo 1. Navigate to the FutureZone directory: cd FutureZone
echo 2. Activate the virtual environment: venv\Scripts\activate
echo 3. Run the bot: python main.py