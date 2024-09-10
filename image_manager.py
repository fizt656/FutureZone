# image_manager.py
import os
import re
import aiohttp
import base64
import io
from PIL import Image
from datetime import datetime
from config import STABLE_DIFFUSION_URL, OPENROUTER_KEY
from characters import characters
import discord

class ImageManager:
    def __init__(self, conversation_manager, character_name):
        self.conversation_manager = conversation_manager
        self.character_name = character_name
        self.image_prompt = characters[character_name]["image_prompt"]
        self.source_faces_folder = characters[character_name]["source_faces_folder"]

    async def generate_selfie_prompt(self, conversation):
        ethnicity_match = re.search(r'\b(?:\d+(?:-year-old)?[\s-]?)?(?:asian|lebanese|black|african|caucasian|white|hispanic|latino|latina|mexican|european|middle eastern|indian|native american|pacific islander|mixed race|biracial|multiracial|[^\s]+?(?=\s+(?:girl|woman|lady|female|man|guy|male|dude)))\b', self.image_prompt, re.IGNORECASE)
        if ethnicity_match:
            ethnicity = ethnicity_match.group()
        else:
            ethnicity = "unknown ethnicity"

        context = ""
        if len(conversation) > 0:
            last_message = conversation[-1]["content"]
            context = f"""Based on the following section from a text adventure game:\n{last_message}\n\nGenerate a short yet decriptive image prompt for Stable Diffusion to create a POV, first person view image of what the player would be seeing at that point in the game. Keep it short, and use words to prompt low-quality photos taken with a phone.
            EXAMPLES:
            a low-quality photo showing a man's office, with a nice futuristic desk and a big TV. dark room, grainy, candid, gritty, blurry, low quality
            
            a selfie of an asian woman posing seductively in a dorm room, dark room, grainy, candid, gritty, blurry, low quality
            
            a low-quality photo showing a garage with an e46 m3 parked inside, with dirty oil stains on the floor, mechanics working on cars in background. dark gritty garage, grainy, candid, gritty, blurry, low quality
"""

#             context = f"""Based on the following conversation:\n{self.image_prompt}{last_message}\n\nGenerate a detailed image prompt for Stable Diffusion to create a selfie of the character in this conversation, considering their ethnicity: {ethnicity}. 
# The prompt should follow this format (change <these parts> to suit the context of the conversation and how the character looks in a selfie now):
# selfie of <describe the character, e.g. 'a 20-year-old asian girl'> <describe what they're wearing and what they're doing', e.g. 'wearing a bikini and lying on a bed with her arms stretched out'>, <describe the place, e.g. 'in a messy bedroom'>

# Keep it short, and use words to prompt low-quality photos taken with a phone.
            # EXAMPLES:
            # selfie of a young american girl wearing a hoodie and glasses under the covers  dark room, grainy, candid, gritty, blurry, low quality
            
            # a selfie of an asian woman wearing a thong and tank top posing seductively in a dorm room, dark room, grainy, candid, gritty, blurry, low quality
# """

        prompt = f"{{image_generation_prompt}}\n{context}"
        messages = [
            {"role": "system", "content": "You are an AI assistant that generates detailed image prompts for Stable Diffusion based on conversation context."},
            {"role": "user", "content": prompt}
        ]

        api_url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "HTTP-Referer": "https://discord.com/api/oauth2/authorize?client_id=1139328683987980288&permissions=1084479764544&scope=bot",
            "X-Title": "my-discord-bot",
            "Content-Type": "application/json"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json={"model": "cohere/command-r-plus", "temperature": 0.5, "max_tokens": 128, "messages": messages}, headers=headers) as response:
                response_json = await response.json()
                if 'choices' in response_json and len(response_json['choices']) > 0:
                    image_prompt = response_json['choices'][0]['message']['content']
                    return image_prompt
                else:
                    return None

    async def generate_image(self, prompt):
        reactor_args = [
            None,  # Placeholder for img_base64
            True,  # Enable ReActor
            '0',  # Comma separated face number(s) from swap-source image
            '0',  # Comma separated face number(s) for target image (result)
            'C:\AI\Forge\stable-diffusion-webui-forge\models\insightface\inswapper_128.onnx',  # Model path
            'CodeFormer',  # Restore Face: None; CodeFormer; GFPGAN
            1,  # Restore visibility value
            True,  # Restore face -> Upscale
            'None',  # Upscaler (type 'None' if doesn't need)
            1.5,  # Upscaler scale value
            1,  # Upscaler visibility (if scale = 1)
            False,  # Swap in source image
            True,  # Swap in generated image
            1,  # Console Log Level (0 - min, 1 - med or 2 - max)
            0,  # Gender Detection (Source) (0 - No, 1 - Female Only, 2 - Male Only)
            0,  # Gender Detection (Target) (0 - No, 1 - Female Only, 2 - Male Only)
            False,  # Save the original image(s) made before swapping
            0.5,  # CodeFormer Weight (0 = maximum effect, 1 = minimum effect), 0.5 - by default
            False,  # Source Image Hash Check, True - by default
            False,  # Target Image Hash Check, False - by default
            "CUDA",  # CPU or CUDA (if you have it), CPU - by default
            True,  # Face Mask Correction
            2,  # Select Source, 0 - Image, 1 - Face Model, 2 - Source Folder
            "elena.safetensors",  # Filename of the face model (from "models/reactor/faces"), e.g. elena.safetensors, don't forget to set #22 to 1
            self.source_faces_folder,  # The path to the folder containing source faces images, don't forget to set #22 to 2
            None,  # skip it for API
            True,  # Randomly select an image from the path
            True,  # Force Upscale even if no face found
            0.6,  # Face Detection Threshold
            2,  # Maximum number of faces to detect (0 is unlimited)
        ]

        payload = {
            "sd_model_checkpoint": "XL_leosamsHelloworldXL_helloworldXL50GPT4V.safetensors",
            "prompt": prompt,
            "steps": 30,
            "sampler_name": "DPM++ 2M Karras",
            "width": 896,
            "height": 1152,
            "seed": -1,
            "guidance_scale": 7,
            "alwayson_scripts": {"reactor": {"args": reactor_args}}
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(STABLE_DIFFUSION_URL, json=payload, headers={'Content-Type': 'application/json'}) as response:
                if response.status == 200:
                    r = await response.json()
                    if 'images' in r and len(r['images']) > 0:
                        image_data = r['images'][0]
                        return image_data
                    else:
                        return None
                else:
                    return None

    async def send_image(self, ctx, image_data):
        image = Image.open(io.BytesIO(base64.b64decode(image_data.split(",", 1)[0])))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_file_name = f"selfie_image_{timestamp}.png"
        image_file_path = os.path.join(self.conversation_manager.subfolder_path, image_file_name)
        image.save(image_file_path)

        with open(image_file_path, "rb") as f:
            await ctx.send(file=discord.File(f, image_file_name))