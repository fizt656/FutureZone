# config_template.py

from characters import characters

# OpenRouter API configuration
OPENROUTER_KEY = 'YOUR_OPENROUTER_KEY'
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_HEADERS = {
    'Authorization': f'Bearer {OPENROUTER_KEY}',
    'HTTP-Referer': 'YOUR_HTTP_REFERER',
    'X-Title': 'Hogwarts-Advisor-Bot',
    'Content-Type': 'application/json'
}

CLAUDE_MODELS = {
    "claude-3-opus-20240229": "3opus",
    "claude-3-5-sonnet-20240620": "35sonnet"
}

OPENROUTER_MODELS = {
    "openai/gpt-4-turbo-preview": "gpt4t",
    "anthropic/claude-3-opus-20240229": "c3opus",
    "google/gemini-pro": "gemini",
    "meta-llama/llama-2-70b-chat": "llama70b",
    "mistralai/mistral-7b-instruct": "mistral7b",
    "huggingfaceh4/zephyr-7b-beta": "zephyr7b"
}
OPENROUTER_MODEL = list(OPENROUTER_MODELS.keys())[0]
OPENROUTER_TEMPERATURE = 0.7
OPENROUTER_MAX_TOKENS = 2048

# Anthropic API configuration
ANTHROPIC_API_KEY = 'YOUR_ANTHROPIC_API_KEY'
ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages'
ANTHROPIC_HEADERS = {
    'X-API-Key': ANTHROPIC_API_KEY,
    'Content-Type': 'application/json',
    'anthropic-version': '2023-06-01'
}
ANTHROPIC_MODEL = 'claude-3-opus-20240229'
ANTHROPIC_MAX_TOKENS = 1024

# Set the default Claude model
DEFAULT_CLAUDE_MODEL = "claude-3-opus-20240229"

# ElevenLabs API configuration
ELEVENLABS_API_KEY = 'YOUR_ELEVENLABS_API_KEY'
ELEVENLABS_API_URL = 'https://api.elevenlabs.io/v1/text-to-speech'
ELEVENLABS_DEFAULT_VOICE_ID = 'YOUR_ELEVENLABS_VOICE_ID'
ELEVENLABS_HEADERS = {
    'Content-Type': 'application/json',
    'xi-api-key': ELEVENLABS_API_KEY,
    'model_id': 'eleven_multilingual_v2',
}
ELEVENLABS_MODEL_ID = 'eleven_multilingual_v2'
ELEVENLABS_VOICE_SETTINGS = {
    'stability': 0.10,
    'similarity_boost': 1,
    'use_speaker_boost': True
}

# Stable Diffusion API configuration
STABLE_DIFFUSION_URL = 'http://127.0.0.1:7860/sdapi/v1/txt2img'

# Discord bot configuration
DISCORD_BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
DISCORD_USER_ID = YOUR_DISCORD_USER_ID  # Replace with the actual user ID

# Default LLM model
DEFAULT_LLM = "anthropic"  # Can be "anthropic", "openrouter", or "lmstudio"