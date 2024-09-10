# tts_manager.py
import os
import re
import aiohttp
from datetime import datetime
from config import ELEVENLABS_API_KEY, ELEVENLABS_MODEL_ID, ELEVENLABS_VOICE_SETTINGS
import discord

class TTSManager:
    def __init__(self):
        self.current_voice_id = None
        self.voice_settings = ELEVENLABS_VOICE_SETTINGS
        self.tts_enabled = False

    def toggle_tts(self):
        self.tts_enabled = not self.tts_enabled

    def set_voice_id(self, voice_id):
        self.current_voice_id = voice_id
        return True

    def get_current_voice_id(self):
        return self.current_voice_id

    async def send_tts(self, channel, text):
        if self.tts_enabled and self.current_voice_id:
            await self.generate_and_send_tts(channel, text)

    async def generate_and_send_tts(self, channel, text):
        headers = {
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
                    await channel.send(file=discord.File(audio_data, 'tts_response.mp3'))
                else:
                    print(f"Error generating TTS: {response.status}")

    async def generate_tts_file(self, text):
        if not self.current_voice_id:
            print("Error: No voice ID set")
            return None

        headers = {
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
                    return tts_file_path
                else:
                    print(f"Error generating TTS: {response.status}")
                    return None