# config_template.py

# Anthropic API configuration
ANTHROPIC_API_KEY = 'YOUR_ANTHROPIC_API_KEY'
ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages'
ANTHROPIC_MODEL = 'claude-3-opus-20240229'
ANTHROPIC_MAX_TOKENS = 1024

# OpenRouter API configuration
OPENROUTER_KEY = 'YOUR_OPENROUTER_KEY'
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'
OPENROUTER_HEADERS = {
    'Authorization': f'Bearer {OPENROUTER_KEY}',
    'HTTP-Referer': 'YOUR_HTTP_REFERER',
    'X-Title': 'TPZ-Advisor-Bot',
    'Content-Type': 'application/json'
}

# Model configurations
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

DEFAULT_CLAUDE_MODEL = "claude-3-opus-20240229"

# ElevenLabs API configuration
ELEVENLABS_API_KEY = 'YOUR_ELEVENLABS_API_KEY'
ELEVENLABS_TTS_URL = 'https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID'
ELEVENLABS_MODEL_ID = 'eleven_multilingual_v2'
ELEVENLABS_VOICE_SETTINGS = {
    'stability': 0.10,
    'similarity_boost': 1,
    'use_speaker_boost': True
}
ELEVENLABS_OUTPUT_FORMAT = 'mp3_44100_192'

# Discord bot configuration
DISCORD_BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
DISCORD_USER_ID = YOUR_DISCORD_USER_ID  # Replace with the actual user ID