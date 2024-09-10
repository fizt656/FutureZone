import asyncio
import discord
from discord.ext import commands
import logging
import argparse

from config import DISCORD_BOT_TOKEN, DISCORD_USER_ID
from conversation_manager import ConversationManager
from api_manager import APIManager
from tts_manager import TTSManager
from characters import characters

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

api_manager = APIManager()
conversation_manager = None
tts_manager = None

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Start the TPZ Advisor bot with a specific character.')
parser.add_argument('character', nargs='?', default='Eli', help='The name of the character to use (default: Eli)')
args = parser.parse_args()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')
    user = await bot.fetch_user(DISCORD_USER_ID)
    
    global conversation_manager, tts_manager, api_manager
    character_name = args.character
    if character_name not in characters:
        print(f"Character '{character_name}' not found. Using default character 'Eli'.")
        character_name = 'Eli'
    
    api_manager.set_character(character_name)
    conversation_manager = ConversationManager(character_name)
    voice_id = characters[character_name]["tts_url"].split('/')[-1]
    voice_settings = characters[character_name]["voice_settings"]
    tts_manager = TTSManager(voice_id, voice_settings)

    await user.send(f"{character_name}, the TPZ Advisor, is ready to help!")

@bot.event
async def on_message(message):
    global conversation_manager, api_manager, tts_manager

    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message)

    # Check if the message is a command
    if message.content.startswith(bot.command_prefix):
        return

    # Check if the message is from the authorized user
    if message.author.id != DISCORD_USER_ID:
        return

    try:
        # Handle conversation and generate response
        response_text = await api_manager.generate_response(message.content, conversation_manager.get_conversation())
        
        if response_text:
            conversation_manager.add_user_message(message.content)
            conversation_manager.add_assistant_response(response_text)

            # Send the response
            response_chunks = conversation_manager.split_response(response_text)
            for chunk in response_chunks:
                await message.channel.send(chunk)

            # Generate and send TTS if enabled
            if tts_manager.tts_enabled:
                await tts_manager.send_tts(message.channel, response_text)
        else:
            await message.channel.send("I apologize, but I couldn't generate a response at this time.")
    
    except Exception as e:
        logger.error(f"Error in on_message: {str(e)}", exc_info=True)
        await message.channel.send("I encountered an unexpected error. Please try again later.")

@bot.command()
async def delete(ctx):
    deleted_message = conversation_manager.delete_last_message()
    if deleted_message:
        await ctx.send("Last message deleted from the conversation.")
    else:
        await ctx.send("No messages to delete.")

@bot.command()
async def clear(ctx):
    conversation_manager.clear_conversation()
    await ctx.send("Conversation history has been cleared.")

@bot.command()
async def tts(ctx):
    tts_manager.toggle_tts()
    if tts_manager.tts_enabled:
        await ctx.send("TTS functionality is now enabled.")
    else:
        await ctx.send("TTS functionality is now disabled.")

@bot.command()
async def say(ctx, *, text=None):
    logger.debug(f"Say command invoked with text: {text}")
    logger.debug(f"TTS enabled: {tts_manager.tts_enabled}")
    
    if tts_manager.tts_enabled:
        if text is None:
            last_message = conversation_manager.get_last_message()
            logger.debug(f"Last message: {last_message}")
            if last_message:
                logger.debug("Attempting to send TTS with last message")
                await tts_manager.send_tts(ctx.channel, last_message)
            else:
                logger.debug("No last message found")
                await ctx.send("There are no messages in the conversation to say.")
        else:
            logger.debug("Attempting to send TTS with provided text")
            await tts_manager.send_tts(ctx.channel, text)
    else:
        logger.debug("TTS is disabled")
        await ctx.send("TTS is currently disabled. Use !tts to enable it.")

@bot.command()
async def quit(ctx):
    await ctx.send("Stopping the bot...")
    await bot.close()

if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)