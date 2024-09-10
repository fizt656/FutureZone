# api_manager.py
import aiohttp
import json
from config import OPENROUTER_URL, ANTHROPIC_URL, OPENROUTER_HEADERS, ANTHROPIC_HEADERS, OPENROUTER_MODELS, CLAUDE_MODELS, DEFAULT_CLAUDE_MODEL, ANTHROPIC_MAX_TOKENS
from characters import characters

class APIManager:
    def __init__(self):
        self.current_llm = "anthropic"
        self.current_claude_model = DEFAULT_CLAUDE_MODEL
        self.current_openrouter_model = list(OPENROUTER_MODELS.keys())[0]
        self.current_character = "Eli"  # Default character

    def set_character(self, character_name):
        if character_name in characters:
            self.current_character = character_name
            return True
        return False

    async def generate_response(self, message, conversation):
        if self.current_llm == "anthropic":
            response_text = await self.generate_anthropic_response(message, conversation)
        elif self.current_llm == "openrouter":
            response_text = await self.generate_openrouter_response(message, conversation)
        else:
            response_text = "Invalid LLM selected."
        return response_text

    async def generate_anthropic_response(self, message, conversation):
        system_prompt = characters[self.current_character]["system_prompt"]
        
        messages = []
        for msg in conversation:
            if msg["role"] != "system":
                messages.append({"role": msg["role"], "content": msg["content"]})
        
        messages.append({"role": "user", "content": message})

        data = {
            "model": self.current_claude_model,
            "messages": messages,
            "system": system_prompt,
            "max_tokens": ANTHROPIC_MAX_TOKENS,
            "temperature": 0.7
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(ANTHROPIC_URL, json=data, headers=ANTHROPIC_HEADERS) as response:
                try:
                    response_json = await response.json()
                    if response.status == 200:
                        if 'content' in response_json:
                            return response_json['content'][0]['text']
                        else:
                            print("Error: 'content' key not found in the Anthropic API response.")
                            print(f"Full response: {json.dumps(response_json, indent=2)}")
                    else:
                        print(f"Error: Anthropic API returned status code {response.status}")
                        print(f"Response headers: {response.headers}")
                        print(f"Response body: {await response.text()}")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    print(f"Response status: {response.status}")
                    print(f"Response headers: {response.headers}")
                    print(f"Response body: {await response.text()}")
                
                return "I apologize, but I encountered an error while processing your request."

    async def generate_openrouter_response(self, message, conversation):
        system_prompt = characters[self.current_character]["system_prompt"]
        full_conversation = [{"role": "system", "content": system_prompt}] + conversation + [{"role": "user", "content": message}]

        async with aiohttp.ClientSession() as session:
            async with session.post(OPENROUTER_URL, json={
                "model": self.current_openrouter_model,
                "messages": full_conversation
            }, headers=OPENROUTER_HEADERS) as response:
                response_json = await response.json()
                if 'choices' in response_json and len(response_json['choices']) > 0:
                    response_text = response_json['choices'][0]['message']['content']
                    return response_text
                else:
                    return "No response generated."

    def switch_llm(self):
        self.current_llm = "openrouter" if self.current_llm == "anthropic" else "anthropic"

    def get_current_llm(self):
        return self.current_llm

    def switch_claude_model(self, model_code):
        for full_name, short_code in CLAUDE_MODELS.items():
            if model_code.lower() == short_code.lower():
                self.current_claude_model = full_name
                self.current_llm = "anthropic"
                return True
        return False

    def switch_openrouter_model(self, model_code):
        for full_name, short_code in OPENROUTER_MODELS.items():
            if model_code.lower() == short_code.lower():
                self.current_openrouter_model = full_name
                self.current_llm = "openrouter"
                return True
        return False

    def get_current_model(self):
        if self.current_llm == "anthropic":
            return self.current_claude_model
        else:
            return self.current_openrouter_model