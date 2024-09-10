# tts_manager.py
import os
import aiohttp
from datetime import datetime
from config import (
    ELEVENLABS_API_KEY,
    ELEVENLABS_API_URL,
    ELEVENLABS_DEFAULT_VOICE_ID,
    ELEVENLABS_HEADERS,
    ELEVENLABS_MODEL_ID
)
import discord
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TTSManager:
    def __init__(self):
        self.current_voice_id = ELEVENLABS_DEFAULT_VOICE_ID
        self.voice_settings = None
        self.tts_enabled = True  # TTS is now enabled by default

    def toggle_tts(self):
        self.tts_enabled = not self.tts_enabled
        logger.info(f"TTS {'enabled' if self.tts_enabled else 'disabled'}")
        return self.tts_enabled

    def set_voice_settings(self, character):
        self.current_voice_id = character.get("tts_url", ELEVENLABS_DEFAULT_VOICE_ID).split('/')[-1]
        self.voice_settings = character.get("voice_settings", {})
        logger.info(f"Voice ID set to: {self.current_voice_id}")
        logger.info(f"Voice settings updated for character")
        return True

    def get_current_voice_id(self):
        return self.current_voice_id

    async def send_tts(self, channel, text):
        if self.tts_enabled:
            logger.info("Generating TTS audio")
            tts_file_path = await self.generate_tts_file(text)
            if tts_file_path:
                await channel.send(file=discord.File(tts_file_path, 'tts_response.mp3'))
                os.remove(tts_file_path)  # Clean up the file after sending
                logger.info("TTS audio sent and file cleaned up")
            else:
                await channel.send("Sorry, I couldn't generate the TTS audio.")
                logger.error("Failed to generate TTS audio")
        else:
            logger.info("TTS is disabled")

    async def generate_tts_file(self, text):
        headers = ELEVENLABS_HEADERS.copy()
        
        data = {
            "text": text,
            "model_id": ELEVENLABS_MODEL_ID,
            "voice_settings": self.voice_settings
        }

        url = f"{ELEVENLABS_API_URL}/{self.current_voice_id}"
        logger.info(f"Sending TTS request to ElevenLabs API")

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status == 200:
                    audio_data = await response.read()
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    tts_file_name = f"tts_response_{timestamp}.mp3"
                    tts_file_path = os.path.join(os.getcwd(), tts_file_name)
                    with open(tts_file_path, 'wb') as f:
                        f.write(audio_data)
                    logger.info(f"TTS audio file generated")
                    return tts_file_path
                else:
                    logger.error(f"Error generating TTS: Status {response.status}")
                    return None