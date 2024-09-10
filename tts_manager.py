# tts_manager.py
import os
import re
import aiohttp
import logging
from datetime import datetime
from config import ELEVENLABS_API_KEY, ELEVENLABS_MODEL_ID
import discord
import io

logger = logging.getLogger(__name__)

class TTSManager:
    def __init__(self, voice_id, voice_settings):
        self.current_voice_id = voice_id
        self.voice_settings = voice_settings
        self.tts_enabled = False
        logger.debug(f"TTSManager initialized with voice ID: {self.current_voice_id}")
        logger.debug(f"Voice settings: {self.voice_settings}")

    def toggle_tts(self):
        self.tts_enabled = not self.tts_enabled
        logger.debug(f"TTS toggled. Enabled: {self.tts_enabled}")

    def set_voice_id(self, voice_id):
        self.current_voice_id = voice_id
        logger.debug(f"Voice ID set to: {self.current_voice_id}")
        return True

    def get_current_voice_id(self):
        return self.current_voice_id

    async def send_tts(self, channel, text):
        logger.debug(f"send_tts called with text: {text[:50]}...")
        if self.tts_enabled and self.current_voice_id:
            logger.debug("TTS is enabled and voice ID is set. Generating TTS...")
            await self.generate_and_send_tts(channel, text)
        else:
            logger.debug(f"TTS not sent. Enabled: {self.tts_enabled}, Voice ID: {self.current_voice_id}")

    async def generate_and_send_tts(self, channel, text):
        logger.debug("Entering generate_and_send_tts method")
        headers = {
            'Accept': 'audio/mpeg',
            'Content-Type': 'application/json',
            'xi-api-key': ELEVENLABS_API_KEY,
        }

        data = {
            "text": text,
            "model_id": ELEVENLABS_MODEL_ID,
            "voice_settings": self.voice_settings
        }

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.current_voice_id}"
        logger.debug(f"Sending request to ElevenLabs API: {url}")
        logger.debug(f"Request data: {data}")

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                logger.debug(f"Received response from ElevenLabs API. Status: {response.status}")
                if response.status == 200:
                    audio_data = await response.read()
                    logger.debug("Successfully received audio data")
                    audio_file = io.BytesIO(audio_data)
                    audio_file.seek(0)
                    await channel.send(file=discord.File(audio_file, 'tts_response.mp3'))
                    logger.debug("Audio file sent to Discord channel")
                else:
                    error_text = await response.text()
                    logger.error(f"Error generating TTS: {response.status}, Response: {error_text}")
                    await channel.send(f"Error generating TTS: {response.status}")

    async def generate_tts_file(self, text):
        if not self.current_voice_id:
            logger.error("Error: No voice ID set")
            return None

        headers = {
            'Accept': 'audio/mpeg',
            'Content-Type': 'application/json',
            'xi-api-key': ELEVENLABS_API_KEY,
        }

        data = {
            "text": text,
            "model_id": ELEVENLABS_MODEL_ID,
            "voice_settings": self.voice_settings
        }

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.current_voice_id}"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status == 200:
                    audio_data = await response.read()
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    tts_file_name = f"tts_response_{timestamp}.mp3"
                    tts_file_path = os.path.join(os.getcwd(), tts_file_name)
                    with open(tts_file_path, 'wb') as f:
                        f.write(audio_data)
                    logger.debug(f"TTS file generated: {tts_file_path}")
                    return tts_file_path
                else:
                    error_text = await response.text()
                    logger.error(f"Error generating TTS file: {response.status}, Response: {error_text}")
                    return None